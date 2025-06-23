{
    "name": "Inoc Base Module",
    "summary": """
        Inoc Base Module
        """,
    "description": """
        Inoc Base Module
        Initializes inoc modules and create inoc app settings menu.
        Add legal address type in contacts
    """,
    "author": "Jofil Inoc Baring <jofil.baring@gmail.com>",
    "website": "https://inoc.me",
    "license": "LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Technical",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "mail"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
    ],
    "application": False,
    "auto_install": True,
}
