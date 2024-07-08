from odoo import models, fields, api, _


class Projects(models.Model):
    _name = 'projects'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Projects'

    name = fields.Char(required=True)
    ref = fields.Char(required=True)
    cost = fields.Float(required=True)
    project_type = fields.Selection([('new', 'New'), ('existing', 'Existing')], required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('start', 'Start'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),])
    description = fields.Html()
    partner_id = fields.Many2one('res.partner', string='Customer')
    time_start = fields.Datetime()
    time_Final = fields.Datetime()

    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('project')
        return super(Projects, self).create(vals)

