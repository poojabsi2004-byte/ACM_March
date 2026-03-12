# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):  # [11-FEB-2026] TASK:Service (Procurement)
    _inherit = 'stock.move'
    _description = 'Stock Move'

    price_subtotal = fields.Float(string="Amount", compute='_compute_amount', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_amount(self):
        for rec in self:
            rec.price_subtotal = rec.price_unit*rec.quantity


class StockPicking(models.Model):  # [11-FEB-2026] TASK:Service (Procurement)
    _inherit = 'stock.picking'

    amount_total = fields.Float(
        string="Total",
        compute="_compute_amount_total",
        store=True,
    )

    @api.depends('move_ids_without_package.price_subtotal')
    def _compute_amount_total(self):
        for picking in self:
            picking.amount_total = sum(
                picking.move_ids_without_package.mapped('price_subtotal')
            )

    delivery_stage = fields.Selection([
        ('chasis_arrival', 'Chasis Arrival'),
        ('chasis_delivery', 'Chasis Delivery'),
        ('edrf', 'EDRF'),
        ('pdi', 'PDI'),
        ('puspakom', 'PUSPAKOM'),
        ('vehicle_registration', 'Vehicle Registration'),
        ('delivered', 'Delivered'),
    ], string="Delivery Stage", tracking=True)

    def chasis_arrival(self):
        self.delivery_stage = 'chasis_arrival'

    def chasis_delivery(self):
        self.delivery_stage = 'chasis_delivery'

    def edrf(self):
        self.delivery_stage = 'edrf'

    def pdi(self):
        self.delivery_stage = 'pdi'

    def puspakom(self):
        self.delivery_stage = 'puspakom'

    def vehicle_registration(self):
        self.delivery_stage = 'vehicle_registration'

    def delivered(self):
        self.delivery_stage = 'delivered'

    new_vehicle_delivery = fields.Boolean(string="New Vehicle Delivery")
