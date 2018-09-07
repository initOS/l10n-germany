from odoo import models, fields, api


class HrDatevEmployeeSurvey(models.Model):
    _name = 'hr.datev.employee.survey'
    _description = u'hr.datev.employee.survey'
    _rec_name = 'employee_id'
    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
        required=True,
        ondelete='set null',
    )

    # personal data tab
    lastname = fields.Char(
        string='lastname',
        related='employee_id.address_home_id.lastname',
        store=True,
    )
    birthname = fields.Char(
        string='birthname',
        related='employee_id.birthname',
        store=True,
    )
    firstname = fields.Char(
        string='firstname',
        related='employee_id.address_home_id.firstname',
        store=True,
    )
    street = fields.Char(
        string='street',
        related='employee_id.address_home_id.street',
        store=True,
    )
    street2 = fields.Char(
        string='street2',
        related='employee_id.address_home_id.street2',
        store=True,
    )
    zip = fields.Char(
        string='zip',
        related='employee_id.address_home_id.zip',
        store=True,
    )
    city = fields.Char(
        string='city',
        related='employee_id.address_home_id.city',
        store=True,
    )
    birthday = fields.Date(
        string='birthday',
        related='employee_id.birthday',
        store=True,
    )
    gender = fields.Selection(
        string='gender',
        related='employee_id.gender',
        store=True,
    )
    insurance_number = fields.Char(
        string='insurance_number',
        related='employee_id.insurance_number',
        store=True,
    )
    marital = fields.Selection(
        string='marital',
        related='employee_id.marital',
        store=True,
    )
    place_of_birth = fields.Char(
        string='place of birth',
        related='employee_id.place_of_birth',
        store=True,
    )
    country_of_birth = fields.Many2one(
        string='country of birth',
        related='employee_id.country_of_birth',
        store=True,
    )
    handicapped = fields.Boolean(
        string='handicapped',
        related='employee_id.handicapped',
        store=True,
    )
    country_id = fields.Many2one(
        string='country',
        related='employee_id.country_id',
        store=True,
    )
    construction_employee_id = fields.Char(
        string='construction employee id',
    )
    bank_id = fields.Many2one(
        string='bank',
        model="res.partner.bank"
    )

    # employment tab
    entry_date = fields.Date(
        string='entry date',
        default=fields.Date.context_today,
    )
    first_entry_date = fields.Date(
        string='first entry date',
        related="employee_id.contract_id.date_start"
    )
    job_title = fields.Char(
        string='job title',
        related='employee_id.job_id.name',
        store=True,
    )
    job_activity = fields.Char(
        string='job activity',
        related='employee_id.job_id.functional_job_activity',
    )
    employment = fields.Selection(
        string='employment',
        related='employee_id.contract_id.employment',
    )
    additional_employment = fields.Boolean(
        string='additional employment',
        related='employee_id.contract_id.additional_employment',
    )
    highest_education = fields.Selection(
        string='highest education',
        related='employee_id.highest_education',
    )
    highest_vet_experience = fields.Selection(
        string='highest vet experience',
        related='employee_id.highest_vet_experience',
    )
    date_start_trainee = fields.Date(
        string='date start trainee',
        default=fields.Date.context_today,
    )
    date_end_trainee = fields.Date(
        string='date end trainee',
        default=fields.Date.context_today,
    )
    construction_business_since = fields.Date(
        string='contruction business since',
        default=fields.Date.context_today,
    )
    cost_centre = fields.Char(
        string='cost_centre',
    )
    production_site = fields.Char(
        string='production site',
    )
    department_number = fields.Char(
        string='department number',
        related='employee_id.department_id.department_number',
    )
    job_activity_number = fields.Char(
        string='job activity number',
        related='employee_id.job_id.job_activity_number',
    )
    leave_count = fields.Char(
        string='leave count',
    )
    working_hour_type = fields.Selection(
        string='working_hour_type',
        related='employee_id.resource_calendar_id.working_hour_type',
    )
    monday_working_hours = fields.Float(
        string='monday_working_hours',
        related='employee_id.resource_calendar_id.monday_working_hours',
    )
    tuesday_working_hours = fields.Float(
        string='tuesday_working_hours',
        related='employee_id.resource_calendar_id.tuesday_working_hours',
    )
    wednesday_working_hours = fields.Float(
        string='wednesday_working_hours',
        related='employee_id.resource_calendar_id.wednesday_working_hours',
    )
    thursday_working_hours = fields.Float(
        string='thursday_working_hours',
        related='employee_id.resource_calendar_id.thursday_working_hours',
    )
    friday_working_hours = fields.Float(
        string='friday_working_hours',
        related='employee_id.resource_calendar_id.friday_working_hours',
    )
    saturday_working_hours = fields.Float(
        string='saturday_working_hours',
        related='employee_id.resource_calendar_id.saturday_working_hours',
    )
    # further_particulars tab
    further_particulars = fields.Char(
        string='further particulars',
    )
    # Ggf.Verteilung d. wöchentl.  resource.calendar.attendance new field
    # field: dayofweek (computed, stored) rel: resource.calendar.attendance_ids

    # limitation
    # Das Arbeitsverhältnis ist befristet / zweckbefristet
    # hr.contract   computed date_start <=> date_end
    limited_employment = fields.Boolean(string='The employment is limited')
    
    # Befristung Arbeitsvertrag zum:
    # hr.contract   if computed => date_end
    limited_employment_date = fields.Boolean(string='Limited to')

    # Schriftlicher Abschluss des befristeten Arbeits...
    # hr.contract   if computed => true
    contract_signed = fields.Boolean(string='The contract was signed')
    
    # Abschluss Arbeitsvertrag am:
    # hr.contract   if computed => date_start
    contract_signed_date = fields.Boolean(string='Signed on')
    
    # befristete Beschäftigung ist ....
    # hr.contract   field: limited_employment_with_designated_employment
    chance_of_continued_employment = fields.Boolean(string='Employment limited to 2 months with a chance of continued employment')
    
    # tax tab
    identification_id = fields.Char(
        string='identification id',
        related='employee_id.identification_id',
    )
    revenue_office_id = fields.Char(
        string='revenue office id',
    )
    tax_class_id = fields.Selection(
        string='tax class id',
        related='employee_id.tax_class_id',
    )
    child_allowance = fields.Float(
        string='child allowance',
        related='employee_id.child_allowance',
    )
    confession = fields.Char(
        string='confession',
        related='employee_id.confession',
    )

    # social insurance tab
    health_ensurance = fields.Char(
        string='health ensurance',
        related='employee_id.health_ensurance',
    )
    parenthood = fields.Boolean(
        string='parenthood',
        related='employee_id.parenthood',
    )
    tax_kv = fields.Float(
        string='tax_kv',
    )
    tax_rv = fields.Float(
        string='tax_rv',
    )
    tax_av = fields.Float(
        string='tax_av',
    )
    tax_pv = fields.Float(
        string='tax_pv',
    )
    tax_uv = fields.Float(
        string='tax_uv',
    )

    # wage tab
    wage_description_1 = fields.Char(
        string='wage_description_1',
    )
    wage_description_2 = fields.Char(
        string='wage_description_2',
    )
    wage_description_3 = fields.Char(
        string='wage_description_3',
    )
    wage_amount1 = fields.Float(
        string='wage_amount1',
    )
    wage_amount2 = fields.Float(
        string='wage_amount1',
    )
    wage_amount3 = fields.Float(
        string='wage_amount1',
    )
    wage_amount_start_date1 = fields.Date(
        string='wage_start_date1',
        default=fields.Date.context_today,
    )
    wage_amount_start_date2 = fields.Date(
        string='wage_start_date1',
    )
    wage_amount_start_date3 = fields.Date(
        string='wage_start_date1',
    )
    wages_per_hour1 = fields.Float(
        string='wages_per_hour1',
    )
    wages_per_hour2 = fields.Float(
        string='wages_per_hour2',
    )
    wages_per_hour3 = fields.Float(
        string='wages_per_hour3',
    )
    wage_hourly_start_date1 = fields.Date(
        string='wage_start_date1',
        default=fields.Date.context_today,
    )
    wage_hourly_start_date2 = fields.Date(
        string='wage_start_date2',
    )
    wage_hourly_start_date3 = fields.Date(
        string='wage_start_date3',
    )

    # vwl tab
    vwl_recipient = fields.Char(
        string='vwl_recipient',
        related='employee_id.address_home_id.name',
    )
