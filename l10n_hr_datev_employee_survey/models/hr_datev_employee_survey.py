# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HrDatevEmployeeSurvey(models.Model):
    _name = 'hr.datev.employee.survey'
    _description = u'hr.datev.employee.survey'

    employee_id = fields.Many2one(
        string=u'Employee',
        comodel_name='hr.employee',
        ondelete='set null',
    )

    # personal data
    lastname = fields.Char(
        string=u'lastname',
        related='employee_id.address_home_id.lastname',
        store=True,
    )
    birthname = fields.Char(
        string=u'birthname',
        related='employee_id.birthname',
        store=True,
    )
    firstname = fields.Char(
        string=u'firstname',
        related='employee_id.address_home_id.firstname',
        store=True,
    )
    street = fields.Char(
        string=u'street',
        related='employee_id.address_home_id.street',
        store=True,
    )
    street2 = fields.Char(
        string=u'street2',
        related='employee_id.address_home_id.street2',
        store=True,
    )
    zip = fields.Char(
        string=u'zip',
        related='employee_id.address_home_id.zip',
        store=True,
    )
    city = fields.Char(
        string=u'city',
        related='employee_id.address_home_id.city',
        store=True,
    )
    birthday = fields.Date(
        string=u'birthday',
        related='employee_id.birthday',
        store=True,
    )
    gender = fields.Selection(
        string=u'gender',
        related='employee_id.gender',
        store=True,
    )
    insurance_number = fields.Char(
        string=u'insurance_number',
        related='employee_id.insurance_number',
        store=True,
    )
    marital = fields.Selection(
        string=u'marital',
        related='employee_id.marital',
        store=True,
    )
    place_of_birth = fields.Char(
        string=u'place of birth',
        related='employee_id.place_of_birth',
        store=True,
    )
    country_of_birth = fields.Many2one(
        string=u'country of birth',
        related='employee_id.country_of_birth',
        store=True,
    )
    handicapped = fields.Boolean(
        string=u'handicapped',
        related='employee_id.handicapped',
        store=True,
    )
    country_id = fields.Many2one(
        string=u'country',
        related='employee_id.country_id',
        store=True,
    )
    construction_employee_id = fields.Char(
        string=u'construction employee id',
    )
    bank_id = fields.Many2one(
        string=u'bank',
        related="employee_id.bank_account_id"
    )

    # employment
    entry_date = fields.Date(
        string=u'entry date',
        default=fields.Date.context_today,
    )
    first_entry_date = fields.Date(
        string=u'first entry date',
        related="employee_id.contract_id.date_start"
    )
    job_title = fields.Char(
        string=u'job title',
        related='employee_id.job_id.name',
        store=True,
    )
    job_activity = fields.Char(
        string=u'job activity',
        related='employee_id.job_id.functional_job_activity',
    )
    employment = fields.Selection(
        string=u'employment',
        related='employee_id.contract_id.employment',
    )
    additional_employment = fields.Boolean(
        string=u'additional employment',
        related='employee_id.contract_id.additional_employment',
    )
    highest_education = fields.Selection(
        string=u'highest education',
        related='employee_id.highest_education',
    )
    highest_vet_experience = fields.Selection(
        string=u'highest vet experience',
        related='employee_id.highest_vet_experience',
    )
    date_start_trainee = fields.Date(
        string=u'date start trainee',
        default=fields.Date.context_today,
    )
    date_end_trainee = fields.Date(
        string=u'date end trainee',
        default=fields.Date.context_today,
    )
    construction_business_since = fields.Date(
        string=u'contruction business since',
        default=fields.Date.context_today,
    )
    cost_centre = fields.Char(
        string=u'cost_centre',
    )
    production_site = fields.Char(
        string=u'production site',
    )
    department_number = fields.Char(
        string=u'department number',
        related='employee_id.department_id.department_number',
    )
    job_activity_number = fields.Char(
        string=u'job activity number',
        related='employee_id.job_id.job_activity_number',
    )
    leave_count = fields.Char(
        string=u'leave count',
    )
    working_hour_type = fields.Selection(
        string=u'working_hour_type',
        related='employee_id.resource_calendar_id.working_hour_type',
    )

    # further_particulars
    further_particulars = fields.Char(
        string=u'further particulars',
    )
    # Ggf.Verteilung d. wöchentl.  resource.calendar.attendance new field
    # field: dayofweek (computed, stored) rel: resource.calendar.attendance_ids

    # limitation
    # Das Arbeitsverhältnis ist befristet / zweckbefristet
    # hr.contract   computed date_start <=> date_end
    # Befristung Arbeitsvertrag zum:
    # hr.contract   if computed => date_end
    # Schriftlicher Abschluss des befristeten Arbeits...
    # hr.contract   if computed => true
    # Abschluss Arbeitsvertrag am:
    # hr.contract   if computed => date_start
    # befristete Beschäftigung ist ....
    # hr.contract   field: limited_employment_with_designated_employment

    # tax
    # Identifikationsnr              hr.employee    field:identification_id
    # Finanzamt-Nr.                  hr.employee new
    # Steuerklasse/Faktor            hr.employee new
    # Kinderfreibeträge              hr.employee new
    # Konfession                     hr.employee new

    # social insurance
    # Gesetzl. Krankenkasse         hr.employee  new

    # Elterneigenschaft             hr.employee  computed children count
    # field: children
    # KV                            l10n_de_payroll needed
    # RV                            l10n_de_payroll needed
    # AV                            l10n_de_payroll needed
    # PV                            l10n_de_payroll needed
    # UV - Gefahrtarif              l10n_de_payroll needed
