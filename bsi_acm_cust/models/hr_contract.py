# -*- coding: utf-8 -*-

from odoo import models, fields


class HrContract(models.Model):
	_inherit = 'hr.contract'

	bond_amount_paid = fields.Monetary(string="Bond Amount", currency_field='currency_id')