from odoo import api, fields, models


class supplier(models.Model):
    _name = 'zulmart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    barang_id = fields.Many2many(comodel_name='zulmart.barang', string='Barang')