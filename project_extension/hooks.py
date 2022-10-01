from odoo import api, SUPERUSER_ID

# def _replace_name(cr, registry):
#     """ This hook is used to add a default buy_pull_id on every warehouse. It is
#     necessary if the purchase_stock module is installed after some warehouses
#     were already created.
#     """
#     print("\n\nCalling from replace method\n\n"*20)
#     env = api.Environment(cr, SUPERUSER_ID, {})
#     cr.execute("update ir_ui_menu set name = REPLACE(name, 'Project', 'Site') where 'name' ilike 'Project%'")
#     cr.execute("update ir_model_fields set field_description = REPLACE(field_description, 'Project', 'Site') where field_description ilike '%Project%'")
#     cr.execute("update ir_act_server set name = REPLACE(name, 'Project', 'Site') where name ilike 'Project%'")
#     cr.execute("update ir_act_window set name = REPLACE(name, 'Project', 'Site') where name ilike 'Project%'")

# def _upgrade_while_uninstallation(cr,registry):
#     env = api.Environment(cr,SUPERUSER_ID,{})
#     # portal_module = env['ir.module.module'].search([('name', '=', 'project')])