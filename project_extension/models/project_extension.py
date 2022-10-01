# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api,tools


class project_extension(models.Model):
    _inherit = 'project.project'

    def init(self):
        """Added the update query to change menu and field name """
        print("\n\ncalling from init project.project\n\n")
        super().init()
        self._cr.execute("""update ir_ui_menu set name = REPLACE(name, 'Project', 'Site') where name ilike '%Project%'""")
        self._cr.execute("""update ir_model_fields set field_description = REPLACE(field_description, 'Project', 'Site') where field_description ilike '%Project%'""")
        self._cr.execute("""update ir_act_server set name = REPLACE(name, 'Project', 'Site') where name ilike '%Project%'""")
        self._cr.execute("""update ir_act_window set name = REPLACE(name, 'Project', 'Site') where name ilike '%Project%'""")
        self._cr.execute("""select id from ir_model_fields imf where field_description ilike '%Task%'""")

        self._cr.execute("""update ir_ui_menu set name = REPLACE(name, 'Task', 'Milestone') where name ilike '%Task%'""")
        self._cr.execute("""update ir_model_fields set field_description = REPLACE(field_description, 'Task', 'Milestone') where field_description ilike '%Task%'""")
        self._cr.execute("""update ir_model_fields set field_description = REPLACE(field_description, 'task', 'Milestone') where field_description ilike '%Task%' or  field_description ilike '%Sub-tasks'""")
        self._cr.execute("""update ir_act_server set name = REPLACE(name, 'Task', 'Milestone') where name ilike '%Task%'""")
        self._cr.execute("""update ir_act_window set name = REPLACE(name, 'Task', 'Milestone') where name ilike '%Task%'""")

    budget = fields.Float('Budget',copy=False)
    project_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ],string='Site size',default='small')
    deadline_date = fields.Datetime(string='Deadline Date', index=True, copy=False)