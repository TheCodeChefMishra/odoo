# -*- coding: utf-8 -*-
{
    'name': "project_extension",

    'summary': """ Extension of project and task module""",

    'description': """
        This module make changes in menu and label of project and task and also 
        reflect changes in tree and kanban view.
    """,
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

    'data': [
        'data/project_data.xml',
        'views/project_extension.xml',
    ],
   # 'post_init_hook': '_replace_name',
   # 'uninstall_hook': '_upgrade_while_uninstallation',
}
