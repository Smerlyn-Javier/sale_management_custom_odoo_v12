from odoo import api, fields, models


class SaleType(models.model):

    _inherit = 'sale.order'
    _inherit = 'fields.model'

    def get_sale_type_inherit(self):
        print('field---->', self.sale_type)
