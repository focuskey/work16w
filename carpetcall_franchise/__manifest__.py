# -*- coding: utf-8 -*-
{
    'name': "carpetcall_franchise",
    'summary': "CarpetCall Franchise Business Type",
    'author': "William WEI",
    "license": "AGPL-3",
    'website': "https://www.carpetcall.com.au",
    "version": "15.0.1.0.0",
    "category": "Services/CarpetCall",
    "depends": ["base"],
    "data": [
        "security/carpetcall_security.xml",
        "security/ir.model.access.csv",
        "views/carpetcall_view.xml",
        "views/carpetcall_menu.xml",
        # "views/carpet_list_template.xml",
        ],
    "application": True,
}