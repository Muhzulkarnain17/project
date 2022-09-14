from odoo import api, fields, models


class Person(models.Model):
    _name = 'zulmart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(String='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'zulmart.kasir'
    _inherit = 'zulmart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID kasir')
    

class cleaningservice(models.Model):
    _name = 'zulmart.cleaningservice'
    _inherit = 'zulmart.person'
    _description = 'New Description'

    id_cln= fields.Char(string='ID cleaningservice')

    