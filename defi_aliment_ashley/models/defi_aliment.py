from odoo import _, api, fields, models


class DefiAliment(models.Model):
    _name = "defi.aliment"
    _description = "defi_aliment"

    name = fields.Char()
