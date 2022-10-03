# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': ' Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    'depends': ['base', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_wizard.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/odoo_playground_view.xml',
        'views/res_config_settings_views.xml',
        'views/operation_view.xml'
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'assets': {},
}
