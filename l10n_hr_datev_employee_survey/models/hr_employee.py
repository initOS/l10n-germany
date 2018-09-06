
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Employee(models.Model):
    
    _inherit = ['hr.employee']

    #Geburtsland

    country_of_birth = fields.Many2one(
        string=u'country_of_birth',
        comodel_name='res.country',
    )
    
    #Geburtsname

    birthname = fields.Char(
        string=u'birth_name',
    )
    
    #Versicherungsnummer
    
    insurance_number = fields.Char(
        string=u'insurance_number',
    )
    
    #Schwerbehindert / Handicapped
    
    handicapped = fields.Boolean(
        string=u'handicapped',
    )
    
    #Höchster Schulabschluss
    
    highest_education = fields.Selection(
        string=u'highest_education',
        selection=[('No Education', 'Lower Secondary Education', 'Secondary Education / Equally High Education', 'Highschool Education')]
    )
    
    #Höchste Berufsbildung
    
    highest_vet_experience = fields.Selection(
        string=u'highest_vet_experience',
        selection=[('No VET', 'Completed VET', '', 'Bachelor', 'Masters Degree', 'Promotion')]
    )

    #Finanzamtnummer

    tax_office_number = fields.Integer(
        string=u'tax_office_number',
    )
    
    #Steuerklasse

    tax_class_id = fields.Selection(
        string=u'tax_class_id',
        selection=[('I (1)', 'II (2)','III (3)', 'IV (4)', 'V (5)', 'VI (6)')]
    )
    
    # Konfession
    
    confession = fields.Char(
        string=u'confession',
    )
    
    # Gesetzliche Krankenkasse
    
    health_ensurance = fields.Char(
        string=u'health_ensurance',
    )

    #Elterneigenschaft
        
    parenthood = fields.Boolean(
        string=u'parenthood',
    )