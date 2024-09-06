from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    va_customer = fields.Boolean(string="Customer")
    va_is_vendor = fields.Boolean(string="Vendor")
