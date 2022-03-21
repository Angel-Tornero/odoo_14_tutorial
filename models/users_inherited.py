from odoo import models, fields, api

class users(models.Model):
    _inherit = "res.users"
    property_ids = fields.One2many("estate.property", "salesperson")