from odoo import api, fields, models, _


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color_2")
    sequence = fields.Integer(string="sequence")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None): #gọi đến phương thức copy
        if default is None:
            default = {}

        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)

        default['sequence'] = 10
        return super(PatientTag, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name', 'unique(name, active)', 'Name must be unique.'),  # Tên của tag không được phép trùng lặp
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be non zero positive number')
        # số của sequence không được nhỏ hơn 1
    ] # đây là cách để loại bỏ sự trùng lặp hoặc có thể dùng @api.constraints
