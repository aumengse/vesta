from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    va_customer = fields.Boolean(string="Customer")
    va_is_vendor = fields.Boolean(string="Vendor")
