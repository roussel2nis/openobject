# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'ACDlec Sale',
    'sequence': 14,
    'summary': 'ACDlec Sale Layout',
    'description': """
ACDlec Sales Reports
====================
    """,
    'author': 'Denis Roussel',
    'website': '',
    'depends': ['sale', 'report','ons_productivity_sale_layout','roussel2nis_webkit_report'],
    'category': 'Sale',
    'data': ['views/report_sale_layout.xml','views/report_invoice_layout.xml'
             
             ],
        'installable': True,
    'application': True,
    'auto_install': False,
}
