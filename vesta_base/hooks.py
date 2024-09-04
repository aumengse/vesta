import os
from typing import Tuple
from odoo import api, SUPERUSER_ID
from odoo.tools import config


def prepare_wh_and_rules(cr, registry):
    """Create a special warehouse and rules for it"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    wh_ids, loc_ids = prepare_warehouses(env)
    prepare_rules(env, wh_ids, loc_ids)


def prepare_warehouses(env) -> Tuple[list[int], list[int]]:
    """Create the Nirvasian warehouse
    return the ids of the warehouse and all it's locations"""
    nirv_warehouse = env["stock.warehouse"].create(
        {"name": "NEXT BASKET PH", "code": "NBPH", "sequence": 1}
    )
    # get the automatically created view location
    nirv_view_location = env["stock.location"].search(
        [("name", "=", "NBPH"), ("usage", "=", "view")]
    )
    # find the automatically created Stock location
    nirv_stock_location = env["stock.location"].search(
        [("location_id", "=", nirv_view_location.id)]
    )
    env["ir.config_parameter"].create(
        [
            {"key": "nirvasian_warehouse_id", "value": nirv_warehouse.id},
            {"key": "nirvasian_view_location_id", "value": nirv_view_location.id},
            {"key": "nirvasian_stock_location_id", "value": nirv_stock_location.id},
        ]
    )
    return nirv_warehouse.ids, nirv_view_location.ids + nirv_stock_location.ids


def prepare_rules(env, wh_ids: list[int], loc_ids: list[int]) -> None:
    # find the inventory admin group (group_stock_manager)
    inventory_admin_group = env.ref("stock.group_stock_manager")
    # the celery user must have all rights as we'll use Celery to get data from Nirvasian API
    celery_user_name = (
        os.environ.get("ODOO_CELERY_USER")
        or config.misc.get("celery", {}).get("user")
        or config.get("celery_user")
    )
    celery_user = env["res.users"].search([("login", "=", celery_user_name)])
    nirv_admin_group = env.ref(
        "nextbasket_nirvasian_integration.group_nirvasian_inventory_admin"
    )
    nirv_admin_group.users = [(4, celery_user.id)]
    # rules for the warehouses
    env["ir.rule"].create(
        [
            {
                "name": "Nirvasian warehouse read only",
                "model_id": env.ref("stock.model_stock_warehouse").id,
                "groups": inventory_admin_group,
                "domain_force": [("id", "not in", wh_ids)],
                "perm_read": False,
            },
            {
                "name": "Nirvasian warehouse admin",
                "model_id": env.ref("stock.model_stock_warehouse").id,
                "groups": nirv_admin_group,
            },
        ]
    )
    # rules for the locations
    env["ir.rule"].create(
        [
            {
                "name": "Nirvasian locations read only",
                "model_id": env.ref("stock.model_stock_location").id,
                "groups": inventory_admin_group,
                "domain_force": [
                    ("id", "not in", loc_ids),
                    ("location_id", "not in", loc_ids),
                ],
                "perm_read": False,
            },
            {
                "name": "Nirvasian locations admin",
                "model_id": env.ref("stock.model_stock_location").id,
                "groups": nirv_admin_group,
            },
        ]
    )
    # rules for warehouse operations
    env["ir.rule"].create(
        [
            {
                "name": "Nirvasian operations read only",
                "model_id": env.ref("stock.model_stock_picking").id,
                "groups": inventory_admin_group,
                "domain_force": [
                    ("location_id", "not in", loc_ids),
                    ("location_dest_id", "not in", loc_ids),
                ],
                "perm_read": False,
            },
            {
                "name": "Nirvasian operations admin",
                "model_id": env.ref("stock.model_stock_picking").id,
                "groups": nirv_admin_group,
            },
        ]
    )
