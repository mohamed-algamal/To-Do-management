# -*- coding: utf-8 -*-
{
    'name': "To Dp Tasks Management",
    'summary': "this project for management task in company",
    'description': """
    """,
    'author': "Mohamed Algamal",
    'category': 'To Do Tasks',
    'version': '1.0.0',
    'depends': ['base','mail'],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        # 'data/mail_template_appointment.xml',
        # 'wizard/cancel_wizard_view.xml',
        'views/menu_views.xml',
        'views/projects_view.xml',
        # 'report/report.xml',
    ],
    'demo': [],
    'excludes': [''],
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
