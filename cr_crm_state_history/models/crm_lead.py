# -*- coding: utf-8 -*-
# Part of Creyox Technologies

from odoo import models, fields, api


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    cr_crm_stage_change_history_ids = fields.One2many(
        comodel_name='cr.crm.stage.change.history',
        inverse_name='crm_lead_id',
        string='cr_stage_change_history_ids',
        groups='cr_crm_state_history.cr_group_access'
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to record initial stage history."""
        records = super(CRMLead, self).create(vals_list)
        for record in records:
            if record.stage_id:
                self.env['cr.crm.stage.change.history'].create({
                    'crm_lead_id': record.id,
                    'stage_name': record.stage_id.name,
                    'date_in': fields.Datetime.now(),
                    'date_in_by_id': self.env.user.id,
                })
        return records

    def write(self, vals):
        """Override write to record stage transition history."""
        if 'stage_id' in vals:
            for record in self:
                # Only record if the stage is actually different
                if record.stage_id.id != vals.get('stage_id'):
                    # Update the previous entry's date_out
                    last_history = self.env['cr.crm.stage.change.history'].search([
                        ('crm_lead_id', '=', record.id)
                    ], limit=1, order='id desc')
                    if last_history:
                        last_history.write({
                            'date_out': fields.Datetime.now(),
                            'date_out_by_id': self.env.user.id,
                        })

                    # Create a new entry for the new stage
                    new_stage = self.env['crm.stage'].browse(vals.get('stage_id'))
                    self.env['cr.crm.stage.change.history'].create({
                        'crm_lead_id': record.id,
                        'stage_name': new_stage.name,
                        'date_in': fields.Datetime.now(),
                        'date_in_by_id': self.env.user.id,
                    })
        return super(CRMLead, self).write(vals)
