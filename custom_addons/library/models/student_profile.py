from odoo import models, fields

class SaleOrder(models.Model):
    _name = 'hgp.student'

    name = fields.Char(string="Name")
    student_id = fields.Char(string="Roll No")
