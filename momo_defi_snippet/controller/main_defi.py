from odoo.odoo import http
import requests

class DefiSnippet(http.Controller):
    @http.route(
        "/momo_defi_snippet/",
        Type="json",
        auth="public",
        website=True,
        method=["POST", "GET"],
    )
    # le client inscrit un fruit et cette methode a prend ce que le client a ecrit
    # et l'ajoute  dans la lsite necessaire
    def defi_snip(self):
        aliments = requests.env["defi.aliment"].searchc([])
        aliments_list = []
        data = {"fruits": aliments_list}
        for element in aliments:
            aliments_list.append(element.name)
        return data
