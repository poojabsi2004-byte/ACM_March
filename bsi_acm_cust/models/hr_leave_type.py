# -*- coding: utf-8 -*-
from odoo import fields, models, api


class hrLeaveYype(models.Model):
    _inherit = "hr.leave.type"
    
    # PP - [13MAR-2026] [ADD] Document Requirement Based on Leave Type [START]
    document_required = fields.Boolean(string="Document Required")
    # PP - [13MAR-2026] [ADD] Document Requirement Based on Leave Type [END]
