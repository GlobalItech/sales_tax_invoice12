#-*- coding:utf-8 -*-

# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from odoo import api, fields, models
from odoo import exceptions, _


class LcReport(models.AbstractModel):
    _name = 'report.sales_tax_invoice.report_lc' #report.modulename.your_modelname of report


    @api.multi
    def _get_report_values(self, docids, data=None):
        

#         pid =comp_sales.partner_id
        acct_invoice = self.env["account.invoice"].search([("id","=",docids)])
        comp_sales = self.env["res.company"].search([('id','=',acct_invoice.company_id.id)])
        if  (acct_invoice.partner_id.supplier == False) or  (acct_invoice.partner_id.supplier == True  and  acct_invoice.partner_id.customer== True):

            pid = acct_invoice.partner_id.id
            cust_invoice = self.env["res.partner"].search([('id','=',pid)])
            table_data = self.env["account.invoice"].search([("id","=",docids)]).invoice_line_ids
    #         data=[]
    #         for d in comp_sales:
    #             data.append(d)
            
            for r in table_data:
                s=0
                for t in r.invoice_line_tax_ids:
                    s= s+t.amount

            return {
                'datas': comp_sales,
                'account': acct_invoice,
                'customer': cust_invoice,
                'table_data': table_data,
                'doc_model': 'account.invoice',
                'proforma': True
            }


        else:
            raise exceptions.ValidationError(_("This Report is only for Sales Order"))

     
     
     
