# -*- coding: utf-8 -*-
{
    'name': "project_validation_extension",

    'summary': """This module developed for custom validation""",

    'description': """This module developed to custom validation which is added in 
    custom requirement module.""",

    'sequence': 999,
    'author': "Port cities",
    'website': "http://www.portcities.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','project_purchase','sale_project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dynamic_requirement_view.xml',
        'views/project_view_extension.xml',
    ],
}
