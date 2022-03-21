# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estates'
    _sql_constraints = [
        (
            'offer_price_positive',
            'CHECK(price > 0)',
            'An offer price must be strictly positive.'
        ),
    ]
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(selection = [('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", required=True, default=False)
    validity = fields.Integer(default = 7)
    create_date = fields.Date(default = fields.Date.today(), readonly = True)
    date_deadline = fields.Date(compute = "_calculate_date_deadline", inverse = "_inverse_calculate_date_deadline")
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", stored = True)

    @api.depends("validity", "create_date")
    def _calculate_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days = record.validity)

    def _inverse_calculate_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    def offer_accept(self):
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer = self.partner_id
    
    def offer_refuse(self):
        self.status = "refused"

    @api.model 
    def create(self, vals):
        if (len(self.env["estate.property"].browse(vals["property_id"]).offer_ids) > 0):
            if (vals["price"] < max(map(lambda i: i.price, self.env["estate.property"].browse(vals["property_id"]).offer_ids))):
                raise UserError("Can't add an offer with a lower price than an existing one.")
        self.env["estate.property"].browse(vals["property_id"]).state = 'offer received'
        return super().create(vals)


