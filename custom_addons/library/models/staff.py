from odoo import models, fields, api, _

class ParentTable(models.Model):
    _name = "hgp.staff"
    _description = "Staff"
    



    staff_id = fields.Char(string="Staff ID")
    staff_name = fields.Char(string="Staff Name")


    
