from odoo import http
from odoo.http import request

class BulkProducts(http.Controller):
	@http.route('/bulk_product_main', type='http', auth="public", website=True)
	def BulkMain(self,**kwargs):
		products_details = request.env['product.product'].search([('detailed_type','=','product')])
		return http.request.render('bulk_products.bulk_products_templates',{'products_details':products_details})

	@http.route('/bulk_products', type='http', auth="public", website=True)
	def Bulk(self,**kwargs):
		product_list = []
		print("---------->>>",kwargs.get('bulk_products_ids'))
		product_list.append(kwargs.get('bulk_products_ids'))
		print("---------->>>",product_list)
		
		user_vals = {
		'name':kwargs.get('user_name'),
		'phone':kwargs.get('phone'),
		'email':kwargs.get('email')
		}
		users = request.env['res.partner'].create(user_vals)

		bulk_vals = {
		'name':kwargs.get('name'),
		'email':kwargs.get('email'),
		'bulk_products_ids':product_list,
		'user_id':users.id
		}

		request.env['bulk.products'].create(bulk_vals)
		# return request.render('bulk_products.bulk_products_templates',{'bulk': bulk})