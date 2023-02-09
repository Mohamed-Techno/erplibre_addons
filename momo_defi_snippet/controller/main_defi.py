from odoo import http
from odoo.http import request
import json
import werkzeug


class DefiSnippet(http.Controller):
    @http.route(
        ["/momo_defi_snippet/defi_aliment"],
        Type="json",
        auth="public",
        website=True,
        method=["POST", "GET"],
        csrf=False
    )
    # le client inscrit un fruit et cette methode a prend ce que le client a ecrit
    # et l'ajoute  dans la lsite necessaire
    def defi_aliment(self):
        aliments = request.env["defi.snip"].search([])
        aliments_list = []
        data = {"fruits": aliments_list}
        for element in aliments:
            aliments_list.append(element.name)
        return data


    @http.route(
        "/momo_defi_snippet/add_aliment",
        type="http",
        auth="user",
        website=True,
        methods=["POST"],
        csrf=False,
    )
    def defi_snip_portal(self, **kw):
        name_values = {}

        if kw.get("ypos"):
            ypos_value = kw.get("ypos")
            name_values["name"] = str(ypos_value)

        new_defi_snip = (
            request.env["defi.snip"].sudo().create(name_values)
        )
