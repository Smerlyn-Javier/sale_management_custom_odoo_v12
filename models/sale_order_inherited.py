from odoo import api, fields, models


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    # Add new fields
    sale_type = fields.Selection(
        [('recorded', 'Recorded'), ('signed', 'Signed')], string='Sale type'
    )
    call_id = fields.Integer(string="Call ID")
