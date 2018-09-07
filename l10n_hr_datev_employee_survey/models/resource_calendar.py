###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api


class ResourceCalendar(models.Model):
    _inherit = 'resource.calendar'

    working_hour_type = fields.Selection(
        string='working hour type',
        selection=[('ft', 'Full Time'), ('pt', 'Part Time')]
    )
