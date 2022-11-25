# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Commission Management',
    'version' : '1.0',
    'summary': 'Commission Management',
    'sequence': 0,
    'description': """Commission Management""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['sale_management','sale'],
    'data': [
    'security/ir.model.access.csv',
    'data/email_sale_inherit.xml',
    'views/commission_view.xml',
    'views/product_commission_view.xml',
    # 'views/supplier_commission_menu.xml',
    'wizard/supplier_commission_view.xml',
    
    'wizard/split_delivery_view.xml',

    # 'data/email_template.xml',
    # 'data/email_inherit.xml',
  
    # 'report/custom_report.xml',
    # 'report/custom_report_template.xml',
    'report/custom_report_inherit.xml',

    'report/custom_design_report.xml',
    'report/custom_design_report_template.xml',

    'report/commission_report.xml',
    'report/commisssion_report_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
