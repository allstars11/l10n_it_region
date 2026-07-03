# -*- coding: utf-8 -*-
{
    'name': 'Italy - Regions',
    'summary': 'Adds the 20 Italian regions as states for Italy',
    'description': """
Italy - Regions
===============
This module adds the 20 Italian administrative regions (regioni) as
res.country.state records linked to Italy, using the ISO 3166-2:IT
region codes (IT-01 through IT-20).

Note: Odoo's base localization already ships the Italian *provinces*
(e.g. Milano, Roma, Torino) as res.country.state records. This module
adds the coarser-grained *regions* (e.g. Lombardia, Lazio, Piemonte)
as additional state records. Both sets coexist since they use
different state codes.
    """,
    'version': '19.0.1.0.0',
    'category': 'Localization',
    'author': 'DigitalForce',
    'website': 'https://www.digitalforce.it',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [
        'data/res_country_state_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
