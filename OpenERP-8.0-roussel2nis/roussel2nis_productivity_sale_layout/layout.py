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

from openerp import models, fields
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
    
    name=fields.Char(string="Name",size=255,required=True)
    text = fields.Text(string="Text")
    type_id = fields.Many2one("sale.predefined.type",string="Type",required=True)
    
    
layout_predefined_text()
