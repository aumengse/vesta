from odoo import fields, models


class DocumentsDocument(models.Model):
    _inherit = "documents.document"

    va_file_category = fields.Selection(
        [
            ("Customer PO", "Customer PO"),
            ("Customer Provided", "Customer Provided"),
            ("Vesta Estimate Source (Legacy)", "Vesta Estimate Source (Legacy)"),
            ("Vesta Estimate Sent (Legacy)", "Vesta Estimate Sent (Legacy)"),
            ("Project Win Document", "Project Win Document"),
            ("Vendor Estimate", "Vendor Estimate"),
            ("Customer Contract", "Customer Contract"),
            ("Customer Safety Notice", "Customer Safety Notice"),
        ],
        string="Category",
    )
    va_file_project = fields.Many2many("project.project", string="Project")
    va_file_salesorder = fields.Many2many("sale.order", string="Sales")
