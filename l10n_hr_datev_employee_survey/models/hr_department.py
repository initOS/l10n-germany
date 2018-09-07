###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api


class Department(models.Model):

    _inherit = 'hr.department'

    # Abt- Nummer
    department_number = fields.Char(
        string='department_number',
    )
