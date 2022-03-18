# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields

class estate_property_tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estates'
    _sql_constraints = [
        (
            'name_unique',
            'UNIQUE(name)',
            'No duplicate tags.'
        )
    ]
    _order = "name"

    name = fields.Char(required = True)
    color = fields.Integer(default = 1)
