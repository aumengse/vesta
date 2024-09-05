from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    va_project_stage = fields.Many2one('project.project.stage', string="Project Stage")
