import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = util.env(cr)
    model = "project.task"

    records = env[model].search([])

    # Iterate over products and update fields
    for rec in records:
        values = {
            "va_project_stage": rec.x_studio_project_stage,
        }
        rec.write(values)
        _logger.info("%s: Data updated for %s", model, rec.name)
