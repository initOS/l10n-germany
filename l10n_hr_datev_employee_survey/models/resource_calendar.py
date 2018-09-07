# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _, exceptions
from odoo.exceptions import UserError, ValidationError


class ResourceCalendar(models.Model):
    _inherit = 'resource.calendar'

    working_hour_type = fields.Selection(
        string=u'working hour type',
        selection=[('ft', 'Full Time'), ('pt', 'Part Time')]
    )
    monday_working_hours = fields.Float(
        string=u'monday_working_hours',
        compute='_compute_working_hours_monday',
    )
    tuesday_working_hours = fields.Float(
        string=u'tuesday_working_hours',
        compute='_compute_working_hours_tuesday',
    )
    wednesday_working_hours = fields.Float(
        string=u'wednesday_working_hours',
        compute='_compute_working_hours_wednesday',
    )
    thursday_working_hours = fields.Float(
        string=u'thursday_working_hours',
        compute='_compute_working_hours_thursday',
    )
    friday_working_hours = fields.Float(
        string=u'friday_working_hours',
        compute='_compute_working_hours_friday',
    )
    saturday_working_hours = fields.Float(
        string=u'saturday_working_hours',
        compute='_compute_working_hours_saturday',
    )

    def _compute_working_hours_monday(self):
        monday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '0':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        monday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.monday_working_hours = monday_hours

    def _compute_working_hours_tuesday(self):
        tuesday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '1':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        tuesday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.tuesday_working_hours = tuesday_hours

    def _compute_working_hours_wednesday(self):
        wednesday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '2':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        wednesday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.wednesday_working_hours = wednesday_hours

    def _compute_working_hours_thursday(self):
        thursday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '3':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        thursday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.thursday_working_hours = thursday_hours

    def _compute_working_hours_friday(self):
        friday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '4':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        friday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.friday_working_hours = friday_hours

    def _compute_working_hours_saturday(self):
        saturday_hours = 0
        for attendance_records in self:
            for attendance in attendance_records.attendance_ids:
                if attendance.dayofweek == '5':
                    if attendance.hour_to < attendance.hour_from:
                        continue
                    elif attendance.hour_from > 24 or attendance.hour_to > 24:
                        continue
                    else:
                        saturday_hours += (attendance.hour_to - attendance.hour_from)
            attendance_records.saturday_working_hours = saturday_hours