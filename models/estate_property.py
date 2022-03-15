# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta

class estate(models.Model):
    _name = 'estate.property'
    _description = 'Estates'

    name = fields.Char(required = True)
    description = fields.Text()
    value = fields.Integer()
    value2 = fields.Float()
    postcode = fields.Char()
    date_availability = fields.Date(default = fields.Date.today() + relativedelta(months = 3), copy = False)
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(default = True)
    state = fields.Selection(
        selection = [('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    buyer = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
