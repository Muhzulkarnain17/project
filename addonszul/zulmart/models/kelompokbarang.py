from odoo import api, fields, models


class KelompoBarang(models.Model):
    _name = 'zulmart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('hp1', 'Samsung'), ('hp2', 'Iphone'), ('hp3', 'Oppo'), ('hp4', 'xiaomi'), ('hp5', 'vivo')
    ], string='nama kelompok')
    
    kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='kode kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self): 
        if (self.name == 'hp1'):
            self.kode_kelompok = 'h1'
        elif (self.name == 'hp2'):
            self.kode_kelompok = 'h2'
        elif (self.name == 'hp3'):
            self.kode_kelompok = 'h3'
        elif (self.name == 'hp4'):
            self.kode_kelompok = 'h4'
        elif (self.name == 'hp5'):
            self.kode_kelompok = 'h5'

        
    kode_rak = fields.Char(string='Tempat Barang')
    barang_ids = fields.One2many(comodel_name='zulmart.barang', inverse_name='kelompokbarang_id', string='daftar barang')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['zulmart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a 
  
    daftar = fields.Char(string='Daftar Barang')

    