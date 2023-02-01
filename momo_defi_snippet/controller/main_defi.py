from odoo.odoo import http
import requests

from odoo.odoo.http import request


class DefiSnippet(http.Controller):
    @http.route(
        ["/momo_defi_snippet/momo_defi_snippet"],
        Type="json",
        auth="public",
        website=True,
        method=["POST", "GET"],
        csrf=False
    )
    # le client inscrit un fruit et cette methode a prend ce que le client a ecrit
    # et l'ajoute  dans la lsite necessaire
    def defi_snip(self):
        aliments = requests.env["defi.snip"].searchc([])
        aliments_list = []
        data = {"fruits": aliments_list}
        for element in aliments:
            aliments_list.append(element.name)
        return data

    @http.route(
        "/momo_defi_snippet/add",
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
            request.env["defi.snip"].sudo().create(vals)
        )
