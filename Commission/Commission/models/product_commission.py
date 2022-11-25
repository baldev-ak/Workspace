from odoo import api, fields, models


class Product(models.Model):
    _inherit = "product.product"

    commission = fields.Float(string = "Commission", default = 5) 

