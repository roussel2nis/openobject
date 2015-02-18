from openerp import models, fields, api

class sale_order(models.Model):
    _inherit='sale.order'
    
    @api.cr_uid_ids_context
    def get_products_from_template(self,cr,uid,order,context=None):
        
        if not context:
            context = {}

        context.update({
            'active_model': self._name,
            'active_ids': order,
            'active_id': len(order) and order[0] or False
        })
        created_id = self.pool['sale.order_template_import'].create(cr, uid, {'order_id': len(order) and order[0] or False}, context)
        
        return self.pool['sale.order_template_import'].wizard_view(cr,uid,created_id,context)
        
        
    
sale_order()

class sale_order_template(models.Model):
    
    _name='sale.order.template'
    
    name = fields.Char('Name',size=64,required=False)
    
    lines = fields.One2many('sale.order.template.line','template')
    
    
sale_order_template()


class sale_order_template_line(models.Model):
    
    _name='sale.order.template.line'
    
    template = fields.Many2one('sale.order.template','Template')
    product = fields.Many2one('product.product','Product')
    quantity = fields.Float('Quantity')
    uom = fields.Many2one('product.uom','Unit',required=True)
    cost_price = fields.Float('Cost Price')
    sale_price = fields.Float('Sale Price')
    
    @api.onchange('product')
    def onchange_product(self):
        self.uom = self.product.uom_id.id
        self.cost_price = self.product.standard_price
        self.sale_price = self.product.list_price
    
    
sale_order_template()