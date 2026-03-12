# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


#[11-FEB-2026] Task:Service Department - Warranty Handling
class VehicleModel(models.Model): 
    _inherit = 'vehicle.model'

    warranty = fields.Float(string="Warranty Years")
    model_code = fields.Char(string="Model Code")
    description = fields.Char(string="Description")
    chasis_number_prefix = fields.Char(string="Chasis Number Prefix")


class InspectionJobCard(models.Model):  
    _inherit = 'inspection.job.card'

    @api.onchange('vehicle_model_id', 'manufacturing_year')
    def _onchange_is_vehicle_under_warranty(self):
        today = date.today()
        for rec in self:
            if rec.manufacturing_year:
                manufacturing_year = int(rec.manufacturing_year)
            else:
                manufacturing_year = 0
            warranty_year = manufacturing_year + (rec.vehicle_model_id.warranty
                                                  or 0)
            if today.year <= warranty_year:
                rec.is_vehicle_under_warranty = True
            else:
                rec.is_vehicle_under_warranty = False


class RepairJobCard(models.Model):
    _inherit = 'repair.job.card'

    @api.onchange('vehicle_model_id', 'manufacturing_year')
    def _onchange_is_vehicle_under_warranty(self):
        today = date.today()
        for rec in self:
            if rec.manufacturing_year:
                manufacturing_year = int(rec.manufacturing_year)
            else:
                manufacturing_year = 0
            warranty_year = manufacturing_year + (rec.vehicle_model_id.warranty
                                                  or 0)
            if today.year <= warranty_year:
                rec.is_vehicle_under_warranty = True
            else:
                rec.is_vehicle_under_warranty = False
