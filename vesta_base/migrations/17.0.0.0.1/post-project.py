import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)

#
# def migrate(cr, version):
#     env = util.env(cr)
#     model = "project.project"
#
#     project_fields = env["ir.model.fields"].search(
#         [
#             ("model", "=", model),
#             ("state", "=", "manual"),
#         ]
#     )
#
#     SET_STR = ", ".join(
#         [
#             "va" + field.name[8:] + " = " + field.name
#             for field in project_fields.filtered(
#                 lambda r: not r.name == "x_studio_contract_value"
#             )
#         ]
#     )
#     query = f"UPDATE {model.replace('.','_')} SET {SET_STR}"
#     cr.execute(query)
#
#     _logger.info("Updated %s fields in model %s ", (len(project_fields), model))


def migrate(cr, version):
    env = util.env(cr)
    model = "project.project"

    records = env[model].search([])

    # Iterate over products and update fields
    for rec in records:
        values = {
            "va_anticipated_completion": rec.x_studio_anticipated_completion,
            "va_award_date": rec.x_studio_award_date,
            "va_comments_legacy": rec.x_studio_comments_legacy,
            "va_complete_cad": rec.x_studio_complete_cad,
            "va_complete_electrical": rec.x_studio_complete_electrical,
            "va_complete_panel": rec.x_studio_complete_panel,
            "va_complete_parts": rec.x_studio_complete_parts,
            "va_complete_prog": rec.x_studio_complete_prog,
            "va_completed_date": rec.x_studio_completed_date,
            # "va_contract_value": rec.x_studio_contract_value,
            "va_cost_to_complete": rec.x_studio_cost_to_complete,
            "va_customer_po": rec.x_studio_customer_po,
            "va_job_id": rec.x_studio_job_id,
            "va_left_to_bill": rec.x_studio_left_to_bill,
            "va_quote_legacy": rec.x_studio_quote_legacy,
            "va_show_design": rec.x_studio_show_design,
            "va_show_field_install": rec.x_studio_show_field_install,
            "va_show_ordering": rec.x_studio_show_ordering,
            "va_show_panel_build": rec.x_studio_show_panel_build,
            "va_show_programming": rec.x_studio_show_programming,
        }
        rec.write(values)
        _logger.info("%s: Data updated for %s", model, rec.name)
