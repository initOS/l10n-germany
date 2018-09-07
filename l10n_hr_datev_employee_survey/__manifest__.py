

###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2018  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'l10n_hr_datev_personalfragebogen',
    'summary': 'l10n_hr_datev_personalfragebogen Module Project',
    'version': '11.0.1.0.0',

    'description': """
l10n_hr_datev_personalfragebogen Module Project.
    """,

    'author': 'Alexander Schubert, Thore Baden',
    'maintainer': 'OCA',
    'contributors': [''],

    'website': '',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base',
        'hr',
        'contacts',
        'base_iban',
        'partner_firstname',
        'hr_holidays',
        'hr_contract',
    ],
    'data': [
        'views/hr_datev_employee_survey.xml',
        'report/hr_datev_employee_survey.xml',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
