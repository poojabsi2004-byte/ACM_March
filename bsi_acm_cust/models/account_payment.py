from odoo import models, fields, api

class AccountPayment(models.Model):
    _inherit = 'account.payment'
    
    # [pp:] - [25MAR-2026] [ADD] Displaying PO Number in Payment Records [START]
    payment_type = fields.Selection(selection=[
        ('outbound', 'Send Payment'),
        ('inbound', 'Receive Payment'),
        ('transfer', 'Internal Transfer'),
    ], string="Payment Type", required=True)
    
    po_number = fields.Char(string="PO Number", compute="_compute_po_no", store=True)

    # [pp:] - [24MAR-2026] [ADD] Displaying PO Number in Payment Records [START]
    @api.depends('reconciled_bill_ids.invoice_origin')
    def _compute_po_no(self):
        for rec in self:
            po_names = set()

            for bill in rec.reconciled_bill_ids:
                if bill.invoice_origin:
                    po_names.add(bill.invoice_origin)

            rec.po_number = ', '.join(po_names) if po_names else False
            
    