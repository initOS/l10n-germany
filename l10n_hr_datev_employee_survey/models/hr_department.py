
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Department(models.Model):

    _inherit = 'hr.department'

    #Abt- Nummer
    
    department_number = fields.Char(
        string=u'department_number',
    )
    