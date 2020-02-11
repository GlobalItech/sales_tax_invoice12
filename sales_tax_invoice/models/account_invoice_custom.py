#This code contains addition of some fields
from odoo import fields, models, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    sal_tax_inv = fields.Char('Sale Tax Invoice')
#     sign_aut = fields.Selection([('Shahid Hassan Sheikh','Shahid Hassan Sheikh'),
#                                  ('Abid Hassan Sheikh','Abid Hassan Sheikh'),
#                                  ('Khalid Hassan Sheikh','Khalid Hassan Sheikh')
#                                  ])


