from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patient', string="Patient", tracking=True)
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today, tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    prescription = fields.Html(string="Prescription")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
