{
    'name': "Ethereum signature",
    'version': '1.0',
    'depends': ['base',
                'sale',
                'sales_team',
                'delivery',
                'barcodes',
                'mail',
                'report',
                'portal_sale',
                'website_portal',
                'website_payment',],
    'author': "Sergey Stepanets",
    'category': 'Application',
    'description': """
    Module for ethereum signature for sale order
    """,
#    'price':110,
#    'currency': 'EUR',
    'data': [
     'views/ethereum_config.xml',
     'views/sale_order.xml',
    ],
}