# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    after_sale = fields.Boolean(string="After Sale")  #[11-FEB - 2026] Task: Separate Sales Menu for Sales and After Sales
    vehicle_sales = fields.Boolean(string="Vehicle Sales")              #[11-FEB-2026] Task: Separate Sales Menu for Sales and After Sales
