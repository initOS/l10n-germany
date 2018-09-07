###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api


class Contract(models.Model):
    _inherit = 'hr.contract'

    employment = fields.Selection(
        string='employment',
        selection=[
            ('main', 'main employment'),
            ('secondary', 'secondary employment')
        ]
    )
    additional_employment = fields.Boolean(
        string='additional employment?',
    )

    contruction_business_since = fields.Date(
        string='contruction business since',
        default=fields.Date.context_today,
    )

    limited_employment_with_designated_employment = fields.Boolean(
        string='limited employment with designated employment',
    )
