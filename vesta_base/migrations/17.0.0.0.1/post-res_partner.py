import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = util.env(cr)
    model = "res.partner"

    records = env[model].search([])

    # Iterate over products and update fields
    for rec in records:
        values = {
            "va_customer": rec.x_studio_customer,
            "va_is_vendor": rec.x_studio_is_vendor,
        }
        rec.write(values)
        _logger.info("%s: Data updated for %s", model, rec.name)
