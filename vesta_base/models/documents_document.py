from odoo import fields, models


class DocumentsDocument(models.Model):
    _inherit = "documents.document"

    va_file_category = fields.Selection([
        ('customer_po', 'Customer PO'),
        ('customer_provided', 'Customer Provided'),
        ('vesta_estimate_source_legacy', 'Vesta Estimate Source (Legacy)'),
        ('vesta_estimate_sent_legacy', 'Vesta Estimate Sent (Legacy)'),
        ('project_win_document', 'Project Win Document'),
        ('vendor_estimate', 'Vendor Estimate'),
        ('customer_contract', 'Customer Contract'),
        ('customer_safety_notice', 'Customer Safety Notice'),
    ], string="Category")
    va_file_project = fields.Many2many('project.project', string="Project")
    va_file_salesorder = fields.Many2many('sale.order', string="Sales")
