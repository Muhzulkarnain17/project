from odoo import api, fields, models


class Barang(models.Model):
    _name = 'zulmart.barang'
    _description = 'New Description'

    name = fields.Char(string='nama barang')
    harga_beli = fields.Integer(string='harga modal',required=True)
    harga_jual = fields.Integer(string='harga jual', required=True)
    kelompokbarang_id= fields.Many2one(comodel_name='zulmart.kelompokbarang', string='kelompok barang')
   

