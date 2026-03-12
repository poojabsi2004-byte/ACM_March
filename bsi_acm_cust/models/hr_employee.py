# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):  #[13-FEB-2026] TASK:Basic Additional Fields in Odoo from VMS Masters
    _inherit = 'hr.employee'
    _description = 'Hr Employee'

    is_a_driver = fields.Boolean(string="Is a Driver")
    licence_type = fields.Char(string="Licence Type")
    nric_number = fields.Char(string="NRIC Number")
    expiry_date = fields.Date(string="Expiry Date")
    trade_plate_no = fields.Char(string="Trade Plate No")
    driver_code = fields.Char(string="Driver Code")
