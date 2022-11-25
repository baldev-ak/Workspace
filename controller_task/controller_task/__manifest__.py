# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Controller Tasks',
    'version' : '1.0',
    'summary': 'Controller Tasks',
    'sequence': 0,
    'description': """Controller Tasks""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['website','crm'],
    'data': [
    'views/portal_template.xml',
    'views/customer_template.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
