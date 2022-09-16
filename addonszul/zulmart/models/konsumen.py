from odoo import api, fields, models


class konsumen(models.Model):
    _inherit = 'res.partner'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
