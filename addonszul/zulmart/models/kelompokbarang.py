from odoo import api, fields, models


class KelompoBarang(models.Model):
    _name = 'zulmart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'), ('makanankering', 'Makanan Kering'), ('minuman', 'Minuman')
    ], string='nama kelompok')
    
    kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='kode kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self): 
        if (self.name == 'makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'

        
    kode_rak = fields.Char(string='kode rak')
    barang_ids = fields.One2many(comodel_name='zulmart.barang', inverse_name='kelompokbarang_id', string='daftar barang')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['zulmart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a 
  
    daftar = fields.Char(string='Daftar Isi')