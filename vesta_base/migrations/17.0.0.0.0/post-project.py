import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = util.env(cr)

    project_fields = env["ir.model.fields"].search(
        [
            ("model", "=", "project.project"),
            ("state", "=", "manual"),
        ]
    )

    SET_STR = ", ".join(
        [
            "va" + field.name[8:] + " = " + field.name
            for field in project_fields.filtered(
                lambda r: not r.name == "x_studio_contract_value"
            )
        ]
    )
    query = f"UPDATE project_project SET {SET_STR}"
    cr.execute(query)

    _logger.info("Updated fields %s", len(project_fields))
