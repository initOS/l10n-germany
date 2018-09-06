# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResourceCalendar(models.Model):

    _inherit = 'resource.calendar'
    
    working_hour_type = fields.Selection(
        string=u'working hour type',
        selection=[('ft', 'Full Time'), ('pt', 'Part Time')]
    )
     