from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    va_anticipated_completion = fields.Char(string="Anticipated Completion (Legacy)")
    va_award_date = fields.Date(string="Award Date")
    va_comments_legacy = fields.Char(string="Comments (Legacy)")
    va_complete_cad = fields.Float(string="CAD")
    va_complete_electrical = fields.Float(string="Electrical")
    va_complete_panel = fields.Float(string="Panel")
    va_complete_parts = fields.Float(string="Parts Rcvd")
    va_complete_prog = fields.Float(string="Prog")
    va_completed_date = fields.Date(string="Completed Date")
    va_contract_value = fields.Monetary(string="Monetary Value")
    va_cost_to_complete = fields.Float(string="Cost to Complete")
    va_customer_po = fields.Text(string="Customer PO(s)")
    va_job_id = fields.Char(string="Job ID")
    va_left_to_bill = fields.Float(string="Left to Bill")
    va_quote_legacy = fields.Text(string="Quote (Legacy)")
    va_show_design = fields.Boolean(string="Show Design")
    va_show_field_install = fields.Boolean(string="Show Field Install")
    va_show_ordering = fields.Boolean(string="Show Ordering")
    va_show_panel_build = fields.Boolean(string="Show Panel Build")
    va_show_programming = fields.Boolean(string="Show Programming")
