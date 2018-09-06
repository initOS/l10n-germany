
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Job(models.Model):

    _inherit = 'hr.job'
    functional_job_activity = fields.Char(string='Functional Job Activity')
    