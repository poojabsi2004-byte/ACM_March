from odoo import models, fields, api

class IrAttachment(models.Model):
    _inherit = "ir.attachment"
    _description = "Ir Attachment"

    # partner_id = fields.Many2one('res.partner', string="Partner")
    owner_id = fields.Many2one('res.users', string="Owner", default=lambda self: self.env.user, readonly=True)


    def check(self, mode, values=None):
        user = self.env.user

        for attachment in self:
            # allow creator
            if attachment.create_uid == user:
                continue

            # allow if attachment belongs to partner where user is manager
            if attachment.res_model == 'res.partner' and attachment.res_id:
                partner = self.env['res.partner'].browse(attachment.res_id)
                print(f"{partner}".center(150,'-'))
                if user in partner.manager_ids:
                    continue

        return super().check(mode, values)