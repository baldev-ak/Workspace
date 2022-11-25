from odoo import api, fields, models
from datetime import date
from odoo.exceptions import UserError, ValidationError

class BulkProducts(models.Model):
    _name = "bulk.products"
    _description = "bulk products"

    name = fields.Char(string="Name")
    # master_product_id = fields.Many2one(comodel_name = "product.template", string = "Master Product")
    bulk_products_ids = fields.Many2many(comodel_name = "product.product", domain = "[('detailed_type','=','product')]")
    user_id = fields.Many2one(comodel_name = "res.partner", string = "User")
    email = fields.Char(string = "Email")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    bulk_product_template = fields.Many2one(comodel_name = "bulk.products", string = "Bulk Products")


    @api.onchange('bulk_product_template')
    def bulk_products_adding(self):
        print("---------------->>>",self.bulk_product_template)
        print("---------------->>>",self.bulk_product_template.bulk_products_ids)

        self.order_line.unlink()
        for record in self.bulk_product_template.bulk_products_ids:
            products = []

            products.append((0,0,{
                'product_id':record.id,
                'product_uom_qty':1,
                'price_unit':record.standard_price
                }))

            print("------------>>> \n", products)
            
            # if self.bulk_product_template:
            self.update({
                'order_line': products or False
                })
