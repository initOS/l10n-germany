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

    _rec_name = 'name'
    _order = 'name ASC'

    #name res.partner.name
    #personal data
    #lastname                res.partner + oca_partner_firstname  field: lastname
    #birthname               hr.employee new field                field: birthname
    #firstname               res.partner + oca_partner_firstname  field: firstname
    #Straße und Hausnummer   res.partner                          field: street
    #inkl. Anschriftenzusatz res.partner                          field: street2
    #PLZ                     res.partner                          field: zip
    #Ort                     res.partner                          field: city
    #Geburtsdatum            hr.employee                          field: birthday
    #Geschlecht              hr.employee                          field: gender
    #Versicherungsnummer     hr.employee new field                field: insurance_number
    #gem. Sozialvers.Ausweis hr.employee                          field: identification_id
    #Familienstand           hr.employee                          field: marital

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
    