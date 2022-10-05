import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta


class CancelAppointmentWizard(models.Model):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment Id",
                                     domain=[('state', '=', 'draft'), ('priority', 'in', (
                                         '0', '1', False))])  # domain sẽ tìm các phần tử có state là draft
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")

    def action_cancel(self):

        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_Days')
        allowed_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
        print("allow =", allowed_date)
        if allowed_date == date.today() or self.appointment_id.state == 'in_consultation':
            raise ValidationError(_("This day can't be cancel because the same day or in consultation"))
        self.appointment_id.state = 'cancel'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }  # check ngày trước khi cho vào trạng thái cancel
