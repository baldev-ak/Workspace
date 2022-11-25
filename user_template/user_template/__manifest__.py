# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'User Controller',
    'version' : '1.0',
    'summary': 'User Controller',
    'sequence': 0,
    'description': """User Controller""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['sale_management','sale','website','web'],
    'data': [
    # 'security/ir.model.access.csv',
    'data/email_template.xml',
    'views/users_template.xml',
    'views/sale_inherit_view.xml'
    ],
    'demo': [],
    'assets': {
        'web.assets_frontend': [
            'user_template/static/src/css/design.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
