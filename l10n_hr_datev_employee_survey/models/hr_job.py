# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Job(models.Model):
    _inherit = 'hr.job'
    job_activity_number = fields.Char(
        string=u'job activity number',
        required=True
    )

    # Ausgeübte Tätigkeit
    functional_job_activity = fields.Char(
        string=u'functional_job_activity',
    )

    # Personengruppe
    group_of_people = fields.Char(
        string=u'group_of_people',
    )
