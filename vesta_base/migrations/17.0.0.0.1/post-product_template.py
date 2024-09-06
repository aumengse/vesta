import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = util.env(cr)
    model = "product.template"

    # Search for all products
    products = env[model].search([])

    # Iterate over products and update fields
    for product in products:
        values = {
            "va_cut_sheet": product.x_studio_cut_sheet,
            "va_cut_sheet_filename": product.x_studio_cut_sheet_filename,
            "va_description": product.x_studio_description,
            "va_mfr_number": product.x_studio_mfr_number,
            "va_preferred_vendor": product.x_studio_preferred_vendor,
            "va_product_code": product.x_studio_product_code,
            "va_suppliers_code": product.x_studio_suppliers_code,
            "va_suppliers_webpage": product.x_studio_suppliers_webpage,
        }
        product.write(values)
        _logger.info("%s: Data updated for %s", model, product.name)
