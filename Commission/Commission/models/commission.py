from odoo import api, fields, models
from datetime import date
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    supplier = fields.Many2one(string="Supplier", comodel_name="res.users")
    total_commission = fields.Float(
        string="Total Commission", compute="_compute__total_commission")

    def action_split_order(self):
        # print("------------------------->>>>>>>Test", self)

        stock_picking = self.env['stock.picking'].search(
            [('sale_id', '=', self.id)])
        # print("----------------------->>>>", stock_picking)
        products_list = []
        for rec in stock_picking:
            for record in rec.move_ids_without_package:
                products_list.append(record.product_id.id)

        # print("-----------",products_list)
        ctx = {
            'product': products_list,
            'sale_id': self.id
        }

        # print("-------------->>>>", ctx)
        action_id = self.env.ref('Commission.order_split_wizard_form').id
        # print("---------------__>>>>>>>>>>\n", action_id)
        return {
            "type": "ir.actions.act_window",
            "res_model": "order.split.wizard",
            "view_type": "form",
            "view_mode": 'form',
            "view_id": action_id,
            "name": "Order Split",
            'target': 'new',
            'context': ctx
        }

    @api.depends('order_line.commission_value')
    def _compute__total_commission(self):
        result = 0
        for record in self.order_line:
            result += record.commission_value
        self.total_commission = result

    # def print_commission_report(self):
    #     print("------------>>>> Test")
    #     return self.env.ref('Commission.action_commission_report').report_action(self)

    # Send mail on click of  button  
    # def send_email_sale_order(self):
    #     template_id = self.env.ref('Commission.send_email_sale_order').id
    #     self.env['mail.template'].browse(template_id).send_mail(self.id,force_send=True)

    # def action_confirm(self):
    #     result = super(SaleOrder,self).action_confirm()

    #     template_id = self.env.ref('Commission.send_email_sale_order').id
    #     self.env['mail.template'].browse(template_id).send_mail(self.id,force_send=True)

    #     return result


    # def send_email_sale_order(self):
    #     template_id = self.env.ref('Commission.send_email_sale_order').id
    #     # print("\n\n\n------------------->>>> 1",template_id)
    #     template = self.env['mail.template'].browse(template_id)
    #     ctx = {
    #         'default_model': 'sale.order',
    #         'default_res_id': self.ids[0],
    #         'default_use_template': bool(template_id),
    #         'default_template_id': template_id,
    #         'default_composition_mode': 'comment',
    #         'mark_so_as_sent': True,
    #         'custom_layout': "mail.mail_notification_paynow",
    #         # 'proforma': self.env.context.get('proforma', False),
    #         # 'force_email': True,
    #         # 'model_description': self.with_context(lang=lang).type_name,
    #     }
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(False, 'form')],
    #         'view_id': False,
    #         'target': 'new',
    #         'context': ctx,
    #     }



    # def action_merge_sale_order(self):
    #     quotations_customers_list = [record.partner_id.id for record in self if record.state == 'draft' ]
    #     print("=================>",quotations_customers_list)

    #     # for record in self:
    #     #     if record.state == 'draft':
    #     #         quotations_customers_list.append(record.partner_id.id)
    #     # # quotations_customers_list = self.partner_id.name

    #     # #Checking if selected quotations have same customer_id by converting into set 
    #     # # which removes duplicate ids

    #     quotations_customers_set = set(quotations_customers_list)
    #     print("=================>",quotations_customers_set)  

    #     if len(quotations_customers_set) == 1:
    #         sale_order_quotations = self.env['sale.order'].search([('id','in',self.ids),('partner_id','in',quotations_customers_list),('state','=','draft')])
    #         print("\n\n\n=======",sale_order_quotations)
    #         order_line_list = []
    #         for record in sale_order_quotations:
    #             for rec in record.order_line:
    #                 order_line_list.append((0,0,{
    #                                     'product_id':rec.product_id.id,
    #                                     'product_uom_qty':rec.product_uom_qty,
    #                                     'price_unit':rec.price_unit,
    #                                     'price_subtotal':rec.price_subtotal
    #                     }))
    #             # record.state = 'cancel'
    #             record.action_cancel()

    #         merge_sale_order = self.env['sale.order'].create({
    #             'partner_id':sale_order_quotations.partner_id.id,
    #             'order_line':order_line_list,
    #             # 'state':'sale'
    #             })
    #         merge_sale_order.action_confirm()
    #         return {
    #                 'type': 'ir.actions.act_window',
    #                 'name':'Sale Order',
    #                 'res_model':'sale.order',
    #                 'domain':[('id','=',merge_sale_order.id)],
    #                 'view_mode': 'form',
    #                 'target':'current'
    #                 }
    #     else:
    #         raise ValidationError("Cannot merge other customers quotations !!")

    def action_confirm(self):
        result = super(SaleOrder,self).action_confirm()

        # For moving order_line to bills account_move
        order_list = []
        for record in self.order_line:
            print("\n----------------->>",record.product_id.id)
            order_list.append((0,0,{'product_id':record.product_id.id,
                                    'quantity':record.product_uom_qty,
                                    'price_unit':record.price_unit,
                                    'price_subtotal':record.price_subtotal
                }))

        move_rec = self.env['account.move'].create({
            'move_type':'in_invoice',
            'partner_id':self.supplier.partner_id,
            'invoice_line_ids': order_list,
            'invoice_date': date.today()
            })


            # self.env['account.move.line'].create({
            #     'product_id':record.product_id.id,
            #     'move_id':move_rec.id
            #     })

        #creating supplier commission bills 
        print("\n\n------------------------->>>>>",self.total_commission)

        vals = [(0,0,{'product_id':39,'price_unit':self.total_commission})]
        move_rec = self.env['account.move'].create({
            'move_type':'in_invoice',
            'partner_id':self.supplier.partner_id,
            'invoice_line_ids': vals,
            'invoice_date': date.today()
            })

        return result