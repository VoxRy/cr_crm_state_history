# -*- coding: utf-8 -*-
# Part of Creyox Technologies
from datetime import datetime
from odoo import models, fields, api


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    cr_crm_stage_change_history_ids = fields.One2many(comodel_name='cr.crm.stage.change.history',
                                                  inverse_name='crm_lead_id',
                                                  string='cr_stage_change_history_ids',
                                                  groups='cr_crm_state_history.cr_group_access')

    @api.onchange('stage_id')
    def stage_history(self):
        """Record stage change history when the stage_id is changed."""
        lines = self.cr_crm_stage_change_history_ids
        length = len(lines)
        # If there are existing records, update the last record's date_out
        if lines:
            count = 0
            for line in lines:
                count = count + 1
                if count == length :
                    line.date_out = datetime.now()
                    line.date_out_by_id = self.env.user.id

        # Prepare a new history entry
        dict = []
        dict.append((0, 0, {
            'crm_lead_id': self.id,
            'stage_name': self.stage_id.name,
            'date_in': datetime.now(),
            'date_in_by_id': self.env.user.id,
        }))
        # Append the new entry to the history list
        self.update({
            'cr_crm_stage_change_history_ids': dict
        })



