# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression


class ProductTemplate(models.Model):  #[13-FEB-2026] TASK:Basic Additional Fields in Odoo from VMS Masters
    _inherit = 'product.template'
    _description = 'Product Template'

    model_id = fields.Many2one("vehicle.model", string="Model")

    # Domain for Sales & After Sales according to product type - Later to enable
    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None):
    #     args = list(args or [])

    #     if self.env.context.get('vehicle_sales_type'):
    #         domain = [('sale_ok', '=', True), ('is_vehicle_part', '=', False),
    #                   ('type', '=', 'consu')]
    #         args = expression.AND([args, domain])

    #     elif self.env.context.get('after_sale_type'):
    #         domain = [
    #             '|', ('is_vehicle_part', '=', True), ('type', '=', 'service')
    #         ]
    #         args = expression.AND([args, domain])

    #     return super()._search(args, offset=offset, limit=limit, order=order)
