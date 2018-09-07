###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    # Geburtsland
    country_of_birth = fields.Many2one(
        string='country_of_birth',
        comodel_name='res.country',
    )

    address_home_id = fields.Many2one(
        'res.partner',
        'Private Address',
        help=('Enter here the private address of the employee, not the one '
              'linked to your company.'),
        groups="hr.group_hr_user",
        required=True,
    )

    # Geburtsname
    birthname = fields.Char(
        string='birth_name',
    )

    # Versicherungsnummer
    insurance_number = fields.Char(
        string='insurance_number',
    )

    # Schwerbehindert / Handicapped
    handicapped = fields.Boolean(
        string='handicapped',
    )

    # Höchster Schulabschluss
    highest_education = fields.Selection(
        string='highest_education',
        selection=[
            ('no_education', 'No Education'),
            ('lower_sec_education', 'Lower Secondary Education'),
            ('sec_education', 'Secondary Education / Equally High Education'),
            ('highschool_education', 'Highschool Education')
        ]
    )

    # Höchste Berufsbildung
    highest_vet_experience = fields.Selection(
        string='highest_vet_experience',
        selection=[
            ('no_vet', 'No VET'),
            ('completed_vet', 'Completed VET'),
            ('placeholder', 'PH'),
            ('bachelor', 'Bachelor'),
            ('masters_degree', 'Masters Degree'),
            ('promotion', 'Promotion')
        ]
    )

    # Steuerklasse
    tax_class_id = fields.Selection(
        string='tax_class_id',
        selection=[
            ('1', 'I (1)'),
            ('2', 'II (2)'),
            ('3', 'III (3)'),
            ('4', 'IV (4)'),
            ('5', 'V (5)'),
            ('6', 'VI (6)')
        ]
    )
    # Kinderfreibeträge
    # child_allowance = fields.Float(
    #     string='child allowance',
    # )

    # Konfession
    confession = fields.Char(
        string='confession',
    )

    # Gesetzliche Krankenkasse
    health_ensurance = fields.Char(
        string='health_ensurance',
    )

    # Elterneigenschaft
    parenthood = fields.Boolean(
        string='parenthood',
    )
