from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital patient"
    _rec_name = "name"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    appointment_id = fields.Many2one("hospital.appointment", string="Appointments")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tag")

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("This Birth not acceptable"))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)  # tự dộng tạo ref theo số trong file sequence

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
            return super(HospitalPatient, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
