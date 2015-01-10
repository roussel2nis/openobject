# -*- coding: utf-8 -*-
#
#  File: layout.py
#  Module: ons_productivity_sale_layout
#
#  Created by cyp@open-net.ch
#
#  Copyright (c) 2013 Open-Net Ltd. All rights reserved.
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import osv, fields
from openerp.tools.translate import _

LAYOUTS_LIST = [
    ('article', 'Product'),
    ('title', 'Title'),
    ('text', 'Note'),
    ('predefined','Predefined Text'),
    ('subtotal', 'Sub Total'),
    ('line', 'Separator Line'),
    ('break', 'Page Break'),
]


class sale_order_line(osv.osv):
    
    _inherit="sale.order.line"
    
    _columns={
              'layout_type':fields.selection(LAYOUTS_LIST, 'Layout type', required=True, select=True),
              'predefined_text_id':fields.many2one("sale.predefined.text",string="Predefined Text"),
              }
    
    
    def predefined_text_change(self, cr, uid, ids, layout_type,predefined_text):
        if layout_type != 'predefined':
            return { 'value':{} }

        vals = {
            'name': '',
            'product_id': False,
            'uos_id': False,
            'account_id': False,
            'price_unit': 0.0,
            'price_subtotal': 0.0,
            'quantity': 0,
            'discount': 0.0,
            'invoice_line_tax_id': False,
            'account_analytic_id': False,
            'product_uom_qty': 0.0,
        }
        vals['name'] = self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).text
        
        cr.execute("Select id from product_uom where name ilike 'unit%%' or name ilike '%%pce%%'")
        row = cr.fetchone()
        if row and row[0]:
            vals.update({
                'product_uom': row[0],
                'product_uos': row[0],
            })
        
        return { 'value': vals }
    
sale_order_line()