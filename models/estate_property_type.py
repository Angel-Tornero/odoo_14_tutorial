# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Estates'
    _order = "sequence"

    name = fields.Char(required = True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Estate")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Estate")
    offer_count = fields.Integer(compute = "_count_offers")
    sequence = fields.Integer(default = 1)

    @api.depends("offer_ids")
    def _count_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
