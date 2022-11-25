from odoo import api, fields, models


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"

    commission_percentage = fields.Float(string = "Commission", readonly =False) 
    commission_value = fields.Float(string = "Commission Value", compute = "_compute_commission_value") 


    @api.depends('commission_percentage','price_subtotal')
    def _compute_commission_value(self):
        for record in self:
            record.commission_value = (record.price_subtotal*record.commission_percentage)/100


    @api.onchange('product_id')
    def default_commission_percentage(self):
        for record in self:
            record.commission_percentage = record.product_id.commission