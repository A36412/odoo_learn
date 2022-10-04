from odoo import models, fields, api


class ResGroups(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self, domain):
        """ Return the non-share groups that satisfy ``domain``. """
        group_id = self.env.ref('project.group_project_task_dependencies').id
        return super(ResGroups, self).get_application_groups(
            domain + [('id', '!=', group_id)])  # Hide user group from user form view
