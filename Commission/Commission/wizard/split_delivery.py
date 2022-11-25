from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class OrderSplitWizard(models.TransientModel):
    _name = 'order.split.wizard'

    product_ids = fields.One2many(
        comodel_name="delivery.product.wizard", inverse_name="split_id", String="Products")

    def default_get(self, vals):
        result = super(OrderSplitWizard, self).default_get(vals)
        products = self.env['product.product'].browse(
            self.env.context.get('product'))
        # print(products)

        sale = self.env['sale.order'].browse(self.env.context.get('sale_id'))
        product_list = []

        for move_rec in sale.picking_ids.move_ids_without_package:
            line = (0, 0, {
                'product_id': move_rec.product_id,
                'move_id': move_rec
            })

            product_list.append(line)

        result.update({
            'product_ids': product_list
        })

        return result

    def button_split_delivery(self):
        sale = self.env['sale.order'].browse(self.env.context.get('sale_id'))

        print("-------------    ", sale)

        transfer = self.env['stock.picking'].search(
            [('sale_id', '=', sale.id)])
        print("------------>>>>transfer", transfer)

        # print("------------>>>>>>>>>", stock_lines_list)
        picking = self.env['stock.picking'].create({
            'sale_id': sale.id,
            'origin': sale.name,
            'partner_id': sale.partner_id.id,
            'scheduled_date': datetime.today(),
            'location_id': 8,
            'location_dest_id': 5,
            'picking_type_id': 2,
        })

        for record in self.product_ids:
            if record.product_selectable == True:
                record.move_id.write({
                    'picking_id': picking
                })

                # product_unlink = self.env['stock.move.line'].search([('sale_id','=',sale.id),('product_id','=',record.product_id.id)])
                # product_unlink.unlink()
                # stock_lines_list.append((0,0,{
                #                         'product_id':record.product_id.id,
                #                         'location_id': 8,
                #                         'product_uom_qty':1.00,
                #                         'forecast_availability':1.00,
                #                         'quantity_done': 0.00,
                #                         # 'product_uom_id':1,
                #                         'name': "Split Delivery",
                #                         'location_dest_id':5
                #         }))

        print("------------------>>>>>>>\n", picking.id)


class DeliveryProductWizard(models.TransientModel):
    _name = 'delivery.product.wizard'

    split_id = fields.Many2one(
        comodel_name="order.split.wizard", string="Order Split")
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product")
    product_selectable = fields.Boolean("Check")
    move_id = fields.Many2one(comodel_name='stock.move', string="Move_ID")
