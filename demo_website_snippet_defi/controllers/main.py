import json

import werkzeug

from odoo import http, models, fields, api
from odoo.http import request


class DemoWebsiteSnippetController(http.Controller):
    @http.route(
        ["/demo_website_snippet_defi/helloworld"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def hello_world(self):
        result_ids = request.env["demo.model.internal"].search([])
        lst_fruit = []
        data = {"fruit": lst_fruit}
        for result_id in result_ids:
            lst_fruit.append(result_id.name)
        return data
    @http.route(
        "/demo_website_snippet_defi/add",
        type="http",
        auth="user",
        website=True,
        methods=["POST"],
        csrf=False,
    )
    def submit_demo_model_portal(self, **kw):
        vals = {}

        if kw.get("ypos"):
            ypos_value = kw.get("ypos")
            vals["name"] = str(ypos_value)

        new_demo_model_portal = (
            request.env["demo.model.internal"].sudo().create(vals)
        )