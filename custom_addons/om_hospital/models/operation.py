from odoo import api, fields, models, _


class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_access = False

    doctor_id = fields.Many2one('res.users', string='Doctor')
