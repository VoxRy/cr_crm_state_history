# -*- coding: utf-8 -*-
# Part of Creyox Technologies
from odoo import models, fields, api

class CrmStageChangeHistory(models.Model):
    _name = 'cr.crm.stage.change.history'

    stage_name = fields.Char(string='Stage Name')
    date_in = fields.Datetime(string='Date In')
    date_in_by_id = fields.Many2one(comodel_name='res.users',string='Date In By')
    date_out = fields.Datetime(string='Date Out')
    date_out_by_id = fields.Many2one(comodel_name='res.users', string='Date Out By')
    day_diff = fields.Integer(string='Day Diff',compute='_compute_day_diff',store=True)
    time_diff = fields.Float(string='Time Diff',compute='_compute_time_diff',store=True)
    total_time_diff = fields.Float(string='Total Time Diff',compute='_compute_total_time_diff',store=True)
    crm_lead_id = fields.Many2one(comodel_name='crm.lead',string='Stage task')

    @api.depends('date_in', 'date_out')
    def _compute_day_diff(self):
        """Compute the time difference in hours between date_in and date_out."""
        for record in self:
            if record.date_in and record.date_out:
                record.day_diff = (record.date_out - record.date_in).days
            else:
                record.day_diff = 0

    @api.depends('date_in', 'date_out')
    def _compute_time_diff(self):
        """Compute the time difference in hours between date_in and date_out."""
        for record in self:
            if record.date_in and record.date_out:
                time_difference = record.date_out - record.date_in
                record.time_diff = time_difference.total_seconds() / 3600
            else:
                record.time_diff = 0.0

    @api.depends('date_in', 'date_out')
    def _compute_total_time_diff(self):
        """Compute the total time difference in minutes between date_in and date_out."""
        for record in self:
            if record.date_in and record.date_out:
                time_difference = record.date_out - record.date_in
                record.total_time_diff = time_difference.total_seconds() / 60
            else:
                record.total_time_diff = 0.0