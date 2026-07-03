# -*- coding: utf-8 -*-
{
    'name': 'Regioni Italiane',
    'summary': 'Aggiunge le 20 regioni italiane come stati per l\'Italia',
    'description': """
Regioni Italiane
=================
Questo modulo aggiunge le 20 regioni amministrative italiane come
record res.country.state collegati all'Italia, utilizzando i codici
ISO 3166-2:IT (da IT-01 a IT-20).

Nota: la localizzazione base di Odoo include già le *province* italiane
(es. Milano, Roma, Torino) come record res.country.state. Questo modulo
aggiunge le *regioni* (es. Lombardia, Lazio, Piemonte), a un livello di
dettaglio piu' ampio, come record di stato aggiuntivi. I due insiemi
convivono senza conflitti poiche' utilizzano codici di stato diversi.

--------------------------------------------------------------------

Italian Regions
================
This module adds the 20 Italian administrative regions (regioni) as
res.country.state records linked to Italy, using the ISO 3166-2:IT
region codes (IT-01 through IT-20).

Note: Odoo's base localization already ships the Italian provinces
(e.g. Milano, Roma, Torino) as res.country.state records. This module
adds the coarser-grained regions (e.g. Lombardia, Lazio, Piemonte)
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
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
