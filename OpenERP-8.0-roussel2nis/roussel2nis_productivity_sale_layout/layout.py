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

from openerp import models, fields, api
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


def layout_val_2_text(layout_type):
    val = _( 'Product' )
    if layout_type == 'title':
        val = _( 'Title' )
    elif layout_type == 'text':
        val = _( 'Note' )
    if layout_type == 'predefined':
        val = _( 'Predefined Text' )
    elif layout_type == 'subtotal':
        val = _( 'Sub Total' )
    elif layout_type == 'line':
        val = _( 'Separator Line' )
    elif layout_type == 'break':
        val = _( 'Page Break' )

    return val

class layout_predefined_type(models.Model):
    _name="sale.predefined.type"
    
    name = fields.Char(string="Name",size=255,requierd=True)
    
layout_predefined_type()


class layout_predefined_text(models.Model):
    _name="sale.predefined.text"
    
    code=fields.Char(string="Code",size=255,required=True)
    name=fields.Char(string="Name",size=255,required=True)
    text = fields.Text(string="Text")
    type_id = fields.Many2one("sale.predefined.type",string="Type",required=True)
    

    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        result=[]
        for predefined_text in self:
            
            result.append((predefined_text.id,"[%s] %s" % (str(predefined_text.code.encode('utf-8')),str(predefined_text.name.encode('utf-8')))))
        return result

    

    @api.model
    def name_search(self,name='', args=None,operator='ilike',context=None,limit=100):
        res = []
        args = list(args or [])
        if not name:
            return super(layout_predefined_text, self).name_search(name, args, operator, limit)
        # optimize out the default criterion of ``ilike ''`` that matches everything
        
        if not (name == '' and operator == 'ilike'):
            args += ['|',(self._rec_name, operator, name),('code', operator, name)]
        
        texts = self.search( args, limit=limit)
       
        return texts.name_get()
    
    
layout_predefined_text()
