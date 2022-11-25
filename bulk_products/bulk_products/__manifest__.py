# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Bulk Products',
    'version' : '1.0',
    'summary': 'Bulk Products',
    'sequence': 0,
    'description': """Bulk Products""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['sale_management','sale','website','web'],
    'data': [
    'security/ir.model.access.csv',
    # 'views/assets.xml',
    'views/bulk_products_view.xml',
    'views/menu_bulk_products.xml',
    'views/bulk_products_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
