# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, AccessError

class DynamicField(models.Model):
    _name = 'dynamic.requirement.field'
    _description = 'dynamic.requirement.field'
    _order = 'sequence,id'


    sequence = fields.Integer(string='Sequence',default=10, help="Gives the sequence order when displaying a list record")
    type = fields.Selection([('site', 'Site'), ('milestone', 'Milestone')], string='Type',required=True)
    name = fields.Char(string='Name', default='New', required=True, index=True,copy=False)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    required_line = fields.One2many('dynamic.requirement.field.line', 'dynamic_id', string='Mandatory Project Line',copy=False, auto_join=True)


class DynamicFieldLine(models.Model):
    _name = 'dynamic.requirement.field.line'
    _description = 'dynamic.requirement.field.line'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence',default=10, help="Gives the sequence order when displaying a list record")
    dynamic_id = fields.Many2one('dynamic.requirement.field', string='Requirement Mandatory Site',ondelete='cascade', index=True, copy=False)
    stage_id = fields.Many2one('project.project.stage', string='Stage', ondelete='restrict',copy=False)
    custom_warning = fields.Char(string='Custom Warning Message',required=True)
    mandatory_fields = fields.Many2many("ir.model.fields", string='Mandatory Fields',copy=False)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

class ProjectProjectInherit(models.Model):
    _inherit='project.project'

    dynamic_required_field = fields.Many2one('dynamic.requirement.field', string='Requirement',copy=False)

    @api.constrains('stage_id')
    def _check_validation(self):
        """Checking the validation while project stage change"""
        for record in self:
            not_set = []
            check_validation_lines = record.dynamic_required_field.required_line.filtered(lambda line: line.stage_id.id == record.stage_id.id).sorted('sequence')
            for line in check_validation_lines:
                check_fields = line.mapped('mandatory_fields').mapped('name')
                check_fields_arr = record.read(check_fields)
                check_fields_arr =  check_fields_arr and check_fields_arr.pop()
                for check_f in check_fields_arr:
                    if not check_fields_arr.get(check_f):
                        not_set.append(record._fields[check_f].string)
                if not_set:
                    warning = line.custom_warning
                    warning = '%s' in warning and str(warning %(", ".join(not_set))) or warning
                    raise UserError(_(warning))

