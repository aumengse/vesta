import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    records = util.records
    xml_ids = [
        # Project views
        "studio_customization.odoo_studio_project__840290f3-5656-417e-afd4-4bc45ae4ae1d",
        "studio_customization.odoo_studio_project__c262e232-dc7e-4f5e-aa2d-5dc25f578cd2"
        # Task views
        "studio_customization.odoo_studio_open_vie_181c9305-2263-448d-a17a-0329a35063db"
        "studio_customization.odoo_studio_project__c262e232-dc7e-4f5e-aa2d-5dc25f578cd2"
        # Product Templates views
        "studio_customization.odoo_studio_product__1cbc4fa4-cb92-4013-aaf7-da3d105eed97"
        "studio_customization.odoo_studio_product__e9524046-ef01-4da3-a74d-d3f07855a430"
        # Partner views
        "studio_customization.odoo_studio_res_part_448aa516-4adf-4f5a-a41e-b092438b52ad"
        # Documents document views
        "studio_customization.odoo_studio_document_265a4f32-4047-4605-8e3a-6e1dcb009646"
    ]


    for xml in xml_ids:
        records.remove_view(cr, xml_id=xml, view_id=None, silent=False, key=None)
        _logger.info("Removed view: %s", xml)
