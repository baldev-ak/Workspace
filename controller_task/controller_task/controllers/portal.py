from odoo import http
from odoo.http import request


class CRMLeadPortal(http.Controller):
    @http.route('/crm_lead', type='http', auth="public", website=True)
    def CRMLead(self, **kwargs):
        lead = request.env['crm.lead'].search([])
        return request.render('controller_task.crm_lead_templates', {'lead': lead})

    @http.route('/crm_lead/<model("crm.lead"):crm>/', type='http', auth="public", website=True)
    def CRM(self, crm, **kwargs):
        return request.render('controller_task.crm_lead_custom', {'crm': crm})

    @http.route('/customer_page', type='http', auth="public", website=True)
    def Orders(self, **kwargs):
        order = request.env['sale.order'].search([])

        return request.render('controller_task.customer_templates', {'order': order})
