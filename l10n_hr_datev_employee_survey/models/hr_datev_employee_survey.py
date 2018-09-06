# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

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
    
    #personal data    
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
    

    #name res.partner.name

    #nur bei fehlender Versicherungs-Nr.
    #Geburtsort              hr.employee                          field: place_of_birth
    # -land                  hr.employee new field                field: country_of_birth
    #Schwerbehindert         hr.employee new field                field: handicapped
    #Staatsangehörigkeit     hr.employee                          field: country_id               
    #Arbeitnehmernummer      ???
    #Kontonummer             res.partner.bank
    #(IBAN)                  res.partner.bank                     field: acc_number
    #Bankleitzahl/Bankb      res.bank                             field: bic          rel:res.partner.bank.bank_id of acc_number

    #employment
    #rel info
    #   contract_id	Current Contract
    #   contract_ids   all contracts
    #Eintrittsdatum Ersteintrittsdatum       hr.contract                   field: date_start   rel: oldest contract or current?!?
    #Betriebsstätte                          ???
    #Berufsbezeichnung                       hr.job                        field: name
    #Ausgeübte Tätigkeit                     hr.job new field              field: functional_job_activity
    #Hauptbeschäftigung Nebenbeschäftigung   hr.contract new field         field: employment
    #Üben Sie weitere Beschäftigungen...     hr.contract new field         field: additional_employment
    #Höchster Schulabschluss                 hr.employee new field         field: 
    #Höchste Berufsausbildung                hr.employee new field         field:
              
    #Beginn der Ausbildung:                  hr.contract                   field: date_start             rel: hr.contract.type_id of "trainee"
    #Voraussichtliches Ende der Ausbildung:  hr.contract                   field: date_end               rel: hr.contract.type_id of "trainee"
    #Im Baugewerbe beschäftigt seit          hr.contract new field         field: contruction_business_since  rel: current contract

    #Wöchentliche Arbeitszeit:    resource.calendar.attendance new field   field: working_hours (computed, stored) rel: resource.calendar.attendance_ids
    #Ggf.Verteilung d. wöchentl.  resource.calendar.attendance new field   field: dayofweek (computed, stored) rel: resource.calendar.attendance_ids

    #Urlaubsanspruch(Kalenderjahr)          hr.employee                    field: leave_count
    #Kostenstelle                           ???
    #Abt.-Nummer                            hr.department new field        field: department_number
    #Personengruppe                         hr.job  new field              field: job_activity_number

    #limitation
    #Das Arbeitsverhältnis ist befristet / zweckbefristet    hr.contract   computed date_start <=> date_end
    #Befristung Arbeitsvertrag zum:                          hr.contract   if computed => date_end
    #Schriftlicher Abschluss des befristeten Arbeits...      hr.contract   if computed => true
    #Abschluss Arbeitsvertrag am:                            hr.contract   if computed => date_start
    #befristete Beschäftigung ist ....                       hr.contract   field: limited_employment_with_designated_employment

    #further_particulars
    further_particulars = fields.Char(
        string=u'further particulars',
    )
    
    #tax
    #Identifikationsnr              hr.employee    field:identification_id
    #Finanzamt-Nr.                  hr.employee new
    #Steuerklasse/Faktor            hr.employee new 
    #Kinderfreibeträge              hr.employee new
    #Konfession                     hr.employee new

    #social insurance
    #Gesetzl. Krankenkasse         hr.employee  new
    #Elterneigenschaft             hr.employee  computed children count field: children
    #KV                            l10n_de_payroll needed
    #RV                            l10n_de_payroll needed
    #AV                            l10n_de_payroll needed
    #PV                            l10n_de_payroll needed
    #UV - Gefahrtarif              l10n_de_payroll needed

