# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class estate(models.Model):
    _name = 'estate.property'
    _description = 'Estates'
    _sql_constraints = [
        (
            'expected_price_positive',
            'CHECK(expected_price > 0)',
            'A property expected price must be strictly positive.'
        ),
        (
            'selling_price_positive',
            'CHECK(selling_price >= 0)',
            'A property selling price must be positive.'
        )
    ]
    _order = "id desc"

    name = fields.Char(required = True)
    description = fields.Text()
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
        selection = [('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default = "new")
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    buyer = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Integer(compute = "_calculate_area")
    best_price = fields.Float(compute = "_get_best_offer")

    @api.depends("living_area", "garden_area")
    def _calculate_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _get_best_offer(self):
        for record in self:
            if (record.offer_ids):
                record.best_price = max(map(lambda i: i.price, record.offer_ids))
            else:
                record.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if (self.garden):
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""
            
    def set_as_sold(self):
        for record in self:
            if (record.state != "canceled"):
                record.state = "sold"
            else:
                raise UserError("You cannot set as Sold a Canceled property.")
    
    def set_as_canceled(self):
        for record in self:
            if (record.state != "sold"):
                record.state = "canceled"
            else:
                raise UserError("You cannot set as Canceled a Sold property.")
    
    @api.constrains("selling_price", "expected_price")
    def selling_price_constraint(self):
        for record in self:
            if (not float_is_zero(record.selling_price, precision_digits = 2) and float_compare(record.selling_price, record.expected_price * 0.9, precision_digits = 2) == -1):
                raise ValidationError("The selling price cannot be lower than 90% of the expected price.")

    def unlink(self):
        for record in self:
            if any((record.state != "New" and record.state != "Cancelled") for record in self):
                raise UserError("Can't delete a property that is not New or Cancelled.")
        return super(models.Model, self).unlink