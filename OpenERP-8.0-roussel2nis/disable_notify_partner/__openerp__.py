##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Disable Notify Partners',
    'version': '1.0',
    'author': 'Denis Roussel',
    'depends': ['mail'],
    'demo': [],
    'description': """
A module that disable default notify by email.
====================================================================

You can now define the following for a product:
-----------------------------------------------
    * Manufacturer
    * Manufacturer Product Name
    * Manufacturer Product Code
    * Product Attributes
    """,
    'data': [
        
    ],
    'auto_install': False,
    'installable': True,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
