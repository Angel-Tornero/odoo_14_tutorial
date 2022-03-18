# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields

class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Estates'
    _order = "sequence"

    name = fields.Char(required = True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Estate")
    sequence = fields.Integer(default = 1)

