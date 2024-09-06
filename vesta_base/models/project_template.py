from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    va_cut_sheet = fields.Binary(string="Cut Sheet")
    va_cut_sheet_filename = fields.Char(string="Filename for Cut Sheet")
    va_description = fields.Char(string="Additional Notes")
    va_mfr_number = fields.Char(string="MFR Number")
    va_preferred_vendor = fields.Selection(
        [("Default", "Default")], string="Preferred Vendor"
    )
    va_product_code = fields.Char(string="Product Code")
    va_suppliers_code = fields.Char(string="Supplier's Code")
    va_suppliers_webpage = fields.Char(string="Supplier's Webpage")
