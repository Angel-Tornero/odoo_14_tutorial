# -*- coding: utf-8 -*-
{
    'name': "estate",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ángel Tornero Hernández",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/property_list.xml',
        'views/actions.xml',
        'views/tag_list.xml',
        'views/menu.xml',
        'views/property_form.xml',
        'views/property_search.xml',
        'views/type_list.xml',
        'views/offer_list.xml',
        'views/form_type.xml',
        'views/form_inherited_user.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
