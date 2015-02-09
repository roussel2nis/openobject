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
              'predefined_text':fields.text(string='Predefined Text Text'),
              'predefined_text_id':fields.many2one("sale.predefined.text",string="Predefined Text"),
              }
    def _prepare_order_line_invoice_line(self, cr, uid, line, account_id=False, context=None):
        """Prepare the dict of values to create the new invoice line for a
           sales order line. This method may be overridden to implement custom
           invoice generation (making sure to call super() to establish
           a clean extension chain).

           :param browse_record line: sale.order.line record to invoice
           :param int account_id: optional ID of a G/L account to force
               (this is used for returning products including service)
           :return: dict of values to create() the invoice line
        """
        res = super(sale_order_line,self)._prepare_order_line_invoice_line(cr,uid,line,account_id,context)
        
        res.update(
                   {'predefined_text':line.predefined_text,
                    'predefined_text_id':line.predefined_text_id.id}
                   )

        return res
    
    def predefined_text_change(self, cr, uid, ids, layout_type,predefined_text):
        if layout_type != 'predefined':
            return { 'value':{} }

        vals = {
            'name': '',
            'predefined_text':'',
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
        vals['name'] = self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).name
        sale_order_lines = self.browse(cr,uid,ids)
        vals['predefined_text']=self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).text
        
        
        if len(sale_order_lines) > 0:
            if (sale_order_lines[0] and (sale_order_lines[0].predefined_text=='' or sale_order_lines[0].predefined_text==False)):
                vals['predefined_text']=self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).text
        #else:
            #vals['predefined_text']=sale_order_lines[0].predefined_text

        cr.execute("Select id from product_uom where name ilike 'unit%%' or name ilike '%%pce%%'")
        row = cr.fetchone()
        if row and row[0]:
            vals.update({
                'product_uom': row[0],
                'product_uos': row[0],
            })
        
        return { 'value': vals }
    
sale_order_line()


class account_invoice_line(osv.osv):
    _inherit = 'account.invoice.line'
    
    _columns = {
        'layout_type':fields.selection(LAYOUTS_LIST, 'Layout type', required=True, select=True),
        'predefined_text':fields.text(string='Predefined Text Text'),
        'predefined_text_id':fields.many2one("sale.predefined.text",string="Predefined Text"),
        }
    
    
    def predefined_text_change(self, cr, uid, ids, layout_type,predefined_text):
        if layout_type != 'predefined':
            return { 'value':{} }

        vals = {
            'name': '',
            'predefined_text':'',
            'product_id': False,
            'uos_id': False,
            #'account_id': False,
            'price_unit': 0.0,
            'price_subtotal': 0.0,
            'quantity': 0,
            'discount': 0.0,
            'invoice_line_tax_id': False,
            'account_analytic_id': False,
            'product_uom_qty': 0.0,
        }
        vals['name'] = self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).name
        sale_order_lines = self.browse(cr,uid,ids)
        vals['predefined_text']=self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).text
        
        
        if len(sale_order_lines) > 0:
            if (sale_order_lines[0] and (sale_order_lines[0].predefined_text=='' or sale_order_lines[0].predefined_text==False)):
                vals['predefined_text']=self.pool.get('sale.predefined.text').browse(cr,uid,predefined_text).text
        #else:
            #vals['predefined_text']=sale_order_lines[0].predefined_text

        cr.execute("Select id from product_uom where name ilike 'unit%%' or name ilike '%%pce%%'")
        row = cr.fetchone()
        if row and row[0]:
            vals.update({
                'product_uom': row[0],
                'product_uos': row[0],
            })
        
        return { 'value': vals }
    
    
    
account_invoice_line()