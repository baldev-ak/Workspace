from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SupplierWizard(models.TransientModel):
    _name = 'supplier.wizard'

    supplier_id = fields.Many2one(comodel_name = "res.users", String = "Supplier")

    def button_supplier_commission(self):
        print("---------------->test    \n",self)
        return self.env.ref('Commission.action_commission_report').report_action(self)
        

