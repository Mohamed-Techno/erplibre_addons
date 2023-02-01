from odoo.odoo import fields
from odoo.odoo.service import model


class DefiSnippet(model.Model):
    _nom = ""
    _desc = ""

    nom = fields.Char()