from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color_2")
    sequence = fields.Integer(string="sequence")
    
    @api.returns('self', lambda value:value.id)
    def copy(self,default=None):
        if default is None:
            default = {}
        
        if not default.get('name'):
            default['name'] = self.name + " (copy)"
        default['sequence'] = 10
        return super(PatientTag, self).copy(default)
    
    _sql_constraints = [
        ('unique_tag_name', 'unique(name, active)', 'Name must be unique.'),  # Tên của tag không được phép trùng lặp
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be non zero positive number')
        # số của sequence không được nhỏ hơn 1
    ]
