from odoo import http, models, fields, api
from odoo.http import request

import json
import werkzeug


class DefiAlimentController(http.Controller):
    @http.route(
        ["/defi_aliment_ashley/defi_aliment"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    # Ajout des fruits du demo_internal
    def defi_aliment(self):
        result_ids = request.env["defi.aliment"].search([])
        lst_fruit = []
        data = {"fruit": lst_fruit}
        for result_id in result_ids:
            lst_fruit.append(result_id.name)
        return data

    @http.route(
        "/defi_aliment_ashley/add",
        type="http",
        auth="user",
        website=True,
        methods=["POST"],
        csrf=False,
    )
    def submit_defi_aliment_portal(self, **kw):
        vals = {}

        if kw.get("ypos"):
            ypos_value = kw.get("ypos")
            vals["name"] = str(ypos_value)

        new_defi_aliment_portal = (
            request.env["defi.aliment"].sudo().create(vals)
        )
