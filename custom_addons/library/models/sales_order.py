from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    my_price = fields.Float(string="My Price", compute="_compute_price", store= True)


    @api.depends('list_price')
    def _compute_price(self):
        for rec in self:
            rec.my_price = rec.list_price * 10
