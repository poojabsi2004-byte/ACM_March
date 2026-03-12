# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model): #[13-FEB-2026] TASK:Basic Additional Fields in Odoo from VMS Masters
    _inherit = 'res.partner'
    _description = 'Res Partner'

    family_size_adults = fields.Integer(string="Family Size Adults")
    childrens = fields.Integer(string="Childrens")
    # co_type = fields.Selection()
    old_ic_no = fields.Char(string="Old IC No")
    new_ic_no = fields.Char(string="New IC No")
    co_regn_no = fields.Char(string="CO Regn No")
    sp_disc_ex_stk = fields.Float(string="Sp. Disc Ex Stkc %")
    spares_disc_indent = fields.Float(string="Spares Disc Indent %")
    ol_disc = fields.Float(string="O/L Disc %")
    msic_code = fields.Char(string="MSIC Code")
    vehicle_discount = fields.Float(string="Vehicle Discount %")
    labour_discount = fields.Float(string="Labour Discount %")
    occupation = fields.Char(string="Occupation")
    it_no = fields.Char(string="IT No")
    credit_period = fields.Float(string="Credit Period")
    monthly_income = fields.Float(string="Monthly Income")

    manager_ids = fields.Many2many('res.users', 'res_users_manager_rel', 'users_id', 'manager_id', string="Managers")
    identity_cards = fields.Many2many('ir.attachment', 'users_identity_attachment_rel', 'users_id', 'attachment_id', string="Identity Cards")
    driving_licenc = fields.Many2many('ir.attachment','user_license_attachment_rel','users_id','attachment_id', string="Driving License")

 
    def _update_attachment_access(self):
        for rec in self:
            attachments = rec.identity_cards | rec.driving_licenc
            for att in attachments:
                att.write({
                    'allowed_user_ids': [(6, 0, rec.manager_ids.ids)],
                    'res_model': 'res.partner',
                    'res_id': rec.id,
                })

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._update_attachment_access()
        return record

    def write(self, vals):
        res = super().write(vals)
        self._update_attachment_access()
        return res


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    allowed_user_ids = fields.Many2many(
        'res.users',
        'attachment_user_rel',
        'attachment_id',
        'user_id',
        string="Allowed Users"
    )