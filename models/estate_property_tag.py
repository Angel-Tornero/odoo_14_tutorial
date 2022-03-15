# -*- coding: utf-8 -*-

from odoo import models, fields

class estate_property_tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estates'
    name = fields.Char(required = True)
