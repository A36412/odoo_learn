from odoo import api, fields, models


class CancelAppointmentWizard(models.Model):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment Id")
    reason = fields.Text(string="Reason")

    def action_cancel(seft):
        return
