# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Contract(models.Model):
    _inherit = 'hr.contract'

    employment = fields.Selection(
        string=u'employment',
        selection=[
            ('main', 'main employment'),
            ('secondary', 'secondary employment')
        ]
    )
    additional_employment = fields.Boolean(
        string=u'additional employment?',
    )

    contruction_business_since = fields.Date(
        string=u'contruction business since',
        default=fields.Date.context_today,
    )

    limited_employment_with_designated_employment = fields.Boolean(
        string=u'limited employment with designated employment',
    )
