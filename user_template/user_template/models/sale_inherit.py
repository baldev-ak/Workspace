from odoo import api, fields, models
from datetime import date
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def send_email_sale_order(self):
        template_id = self.env.ref('user_template.send_email_sale_order')
        attachment = self.env['ir.attachment'].search([('res_model','=','sale.order')])
        print("\n\n\n=========================",attachment)
        print("\n\n\n------------------->>>> 1",template_id)
        template = self.env['mail.template'].browse(template_id)

        template_id.attachment_ids = [(4, attachment[0].id)]

        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id.id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            # 'attachment_ids':[583,604,602]
            # 'proforma': self.env.context.get('proforma', False),
            # 'force_email': True,
            # 'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
