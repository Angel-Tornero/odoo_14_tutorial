# -*- coding: utf-8 -*-

from odoo import models, fields

class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Estates'
    name = fields.Char(required = True)
