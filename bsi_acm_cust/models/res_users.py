# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsers(models.Model): #[13-FEB-2026] TASK:Basic Additional Fields in Odoo from VMS Masters
	_inherit = "res.users"
	_description = "Res Users"

	code = fields.Char(string="Code")

	