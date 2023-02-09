from odoo import _, api, fields, models


class DefiSnippet(models.Model):
    _name = "defi.snip"
    _description = "patate"

    name = fields.Char()