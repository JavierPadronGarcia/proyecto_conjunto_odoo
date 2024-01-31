# -*- coding: utf-8 -*-
{
    'name': "proyecto_javier",

    'summary': """
        Aplicación personalizada que sirva de apoyo a una empresa de desarrollo de software
    """,

    'description': """
        Se pretende crear una aplicación personalizada que sirva
        de apoyo a una empresa de desarrollo de software, de 
        la que vamos a ir explicando en este documento cuál es su operativa diaria.
    """,

    'author': "Javier",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/task_stage_data.xml',
        'reports/proyecto_javier_report.xml',
        'reports/proyecto_javier_report_view.xml',
        'security/proyecto_javier_reglas_registro.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',
    'assets': {
        'web.assets_common': [
            'proyecto_javier/static/src/scss/style1.scss'
        ]
    }
}
