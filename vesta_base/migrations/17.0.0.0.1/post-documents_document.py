import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = util.env(cr)
    model = "documents.document"

    records = env[model].search([])

    # Iterate over products and update fields
    for rec in records:
        values = {
            "va_file_category": rec.va_file_category,
            "va_file_project": rec.va_file_project,
            "va_file_salesorder": rec.x_studio_file_salesorder,
        }
        rec.write(values)
        _logger.info("%s: Data updated for %s", model, rec.name)
