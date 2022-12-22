from odoo import api, fields, models


class ResConfigSettingsInherited(models.TransientModel):
    _inherit = 'res.config.settings'

    # Add config field
    res_call_id = fields.Boolean(string='Call ID')
