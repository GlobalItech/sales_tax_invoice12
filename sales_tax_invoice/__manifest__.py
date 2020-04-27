
{

    'name': 'Sales Tax Invoice',
    'category': 'Invoices',
    'summary': 'Pakistan Sales Tax Invoice',
    'description': "This module will be give sale tax invoices print. ",
    'author': 'Itech resources',
    'website': 'www.itechresources.com',
    'depends' : [
                    'account','base','product'
                ],
    'data' :[
                'views/account_invoice_views_custom.xml',
                'views/res_company_custom.xml',
                'views/res_partner_custom.xml',
#                 'views/product_template_custom.xml',
                'reports/lc_report_menu.xml',
                'reports/report1.xml',
                 'reports/header_sti_report.xml',
            ],
    'images': ['static/description/banner.gif'],  
    'installable' : True,
    'price': 20.00,
     'license': 'AGPL-3',
    'currency': 'EUR',

}
