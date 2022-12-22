{
    'name': 'Sale management custom',
    'summary': "Sale management custom",
    'description': "Sale management custom CM test",
    'author': "Smerlyn Javier",
    'license': "AGPL-3",
    'category': 'Sales Management',
    'version': '12.0',
    'depends': ['sale_management'],
    'application': True,
    'installable': True,
    'data': [
        'views/sale_order_inherited.xml',
        'views/res_config_settings_inherited.xml',
    ],
}
