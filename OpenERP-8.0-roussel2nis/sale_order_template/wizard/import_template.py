# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2010 Yannick Soldati. All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class import_template(models.TransientModel):
    
    _name = 'sale.order_template_import'
    _description = "Sale Template Import"
    
    order_id = fields.Many2one('sale.order', 'Order')
    
    template = fields.Many2one('sale.order.template')
    
  
    
    @api.multi
    def wizard_view(self):
        view = self.env.ref('sale_order_template.view_get_products_template')
        
        return {
            'name': 'Import',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.order_template_import',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.ids[0],
            'context': self.env.context,
        }
        
    @api.one
    def import_products(self):
        values={}
        if self.order_id:
            values['order_id']=self.order_id.id
            for line in self.template.lines:
                values['product_id'] = line.product.id
                values['product_uom'] = line.uom.id
                values['product_uom_qty'] = line.quantity
                
                values.update(self.env['sale.order.line'].product_id_change(self.order_id.pricelist_id.id, line.product.id,
                        line.quantity, line.uom.id, 0, False, '',
                        self.order_id.partner_id.id, False, True,
                        self.order_id.date_order, False,
                        self.order_id.fiscal_position.id, False)['value'])
                values['tax_id'] = [(6, 0, values['tax_id'])]
                self.env['sale.order.line'].create(values)
        
        return True
        
            
    
    def _process(self):
        return
        '''
        pool = pooler.get_pool(cr.dbname)
        values = {'order_id': data['id']}

        sale_obj = pool.get('sale.order')
        template_obj = pool.get('sale.order.template')

        template = template_obj.browse(cr, uid, data['form']['template'],
                                       context=context)
        sale = sale_obj.browse(cr, uid, data['id'], context=context)

        for line in template.lines:
            values['product_id'] = line.product.id
            values['product_uom'] = line.uom.id
            values['product_uom_qty'] = line.quantity
            
            values.update(pool.get('sale.order.line').product_id_change(cr,
                    uid, False, sale.pricelist_id.id, line.product.id,
                    line.quantity, line.uom.id, 0, False, '',
                    sale.partner_id.id, False, True,
                    sale.date_order, False,
                    sale.fiscal_position.id, False)['value'])
            values['tax_id'] = [(6, 0, values['tax_id'])]
            pool.get('sale.order.line').create(cr, uid, values)

        return {}

    states = {
        'init': {
            'actions': [],
            'result': {'type': 'form', 'arch': form, 'fields': fields,
                    'state': (('end', 'Concel'), ('process', 'Process'))},
        },
        'process': {
            'actions': [_process],
            'result': {'type': 'state', 'state': 'end'},
        },
    }
    '''

