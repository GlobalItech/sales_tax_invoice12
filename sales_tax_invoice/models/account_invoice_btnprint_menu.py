from odoo import api, exceptions, fields, models, _
from odoo.models import BaseModel

class btn_print_account_invoice(models.Model):
    _inherit="account.invoice"
    
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        def get_view_id(xid, name):
            try:
                return self.env.ref('account.' + xid)
            except ValueError:
                view = self.env['ir.ui.view'].search([('name', '=', name)], limit=1)
                if not view:
                    return False
                return view.id

        context = self._context
        supplier_form_view_id = get_view_id('invoice_supplier_form', 'account.invoice.supplier.form').id
        if context.get('active_model') == 'res.partner' and context.get('active_ids'):
            partner = self.env['res.partner'].browse(context['active_ids'])[0]
            if not view_type:
                view_id = get_view_id('invoice_tree', 'account.invoice.tree')
                view_type = 'tree'
            elif view_type == 'form':
                if partner.supplier and not partner.customer:
                    view_id = supplier_form_view_id
                elif partner.customer and not partner.supplier:
                    view_id = get_view_id('invoice_form', 'account.invoice.form').id
        
        #act=self._context.get('active_id',False)
        act=self.env.context.get('active_ids', [])
        if act != []:
            a=""
            va=[]
        ret=super(btn_print_account_invoice, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        view_id = ret.get('view_id', False)
        if  (self.env['ir.ui.view'].search([('id','=',ret.get('view_id'))]).name=="account.invoice.supplier.form") or  (self.env['ir.ui.view'].search([('id','=',ret.get('view_id'))]).name=="account.invoice.supplier.tree"):
            print_menu=ret.get('toolbar')
            p=ret.get('toolbar')
            pt=[item for item in p['print'] if item['display_name'] == 'Sales Tax Invoice']
            p['print'].remove(pt[0])
#         if ret.get('toolbar', False):
#             reports = ret['toolbar']['print'][:] # Pass by value
#             i = 0
#             for report in reports:
#                 if report['views_id']:
#                     if view_id not in report['views_id']:
#                         ret['toolbar']['print'].pop(i)
#                         i = i-1
#                 i = i+1
        return ret 