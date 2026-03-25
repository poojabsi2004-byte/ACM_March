# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrLeave(models.Model):
    _inherit = "hr.leave"

    # PP - [13MAR-2026] [ADD] Document Requirement Based on Leave Type [START]
    @api.constrains('supported_attachment_ids','name', 'notes')
    def _check_document_required(self):
        for rec in self:
            if rec.holiday_status_id.document_required:
                if len(rec.supported_attachment_ids) < 1:
                    raise ValidationError(
                        "Supporting document is required for this leave type."
                    )
    # PP - [13MAR-2026] [ADD] Document Requirement Based on Leave Type [END]
