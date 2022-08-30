# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': ' Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'assets': {},
}
