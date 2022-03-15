# -*- coding: utf-8 -*-

from odoo import models, fields

class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estates'
    price = fields.Float()
    status = fields.Selection(selection = [('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)