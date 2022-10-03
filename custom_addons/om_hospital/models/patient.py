from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital patient"
    _rec_name = "name"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_compute_age", search="_search_age",
                         tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    appointment_id = fields.Many2one("hospital.appointment", string="Appointments")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tag")
    appointment_count = fields.Integer(string="Appointment_Count", compute="_compute_appointment_count", store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Marital Status",
                                      tracking=True)
    partner_name = fields.Char(string="Partner Name")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count(
                [('patient_id', '=', rec.id)])  # đếm số lượng cuộc họp mà có patient_id = rec.id

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("This Birth not acceptable"))
                # Check ngày sinh nếu ngày sinh lớn hơn thời gian hiện tại thì sẽ xảy ra lỗi

    @api.ondelete(at_uninstall=False)  # Kiểm tra trước khi xóa  Patient xem có còn appointment nào thuộc Patient đó
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You can not delete the Patient with appointment"))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)  # tự dộng tạo ref theo số trong file sequence

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)  # Khi sửa check nếu ref khong co thì nó sẽ sinh ra ref tự động

    @api.depends('date_of_birth')
    def _compute_age(self):  # Đây là hàm tính toán ngày sinh
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        return [('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]
        # Hàm tìm kiếm age vì compyte không lưu vào database => search không thể tìm => đây là trường dùng để tìm trường không lưu trữ

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in
                self]  # %s là vị trí sẽ hiện trong string việc record.id đứng ở đầu
        # là do nó sẽ tìm kếm những phần tử có id đó rồi thềm ref và name vào string theo %s

    def action_test(self):
        print("Haiz")
        return
