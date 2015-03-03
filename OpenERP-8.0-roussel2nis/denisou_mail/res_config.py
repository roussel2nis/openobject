from openerp import fields, models, api
from openerp.tools.safe_eval import safe_eval

class res_config(models.TransientModel):
    _name= 'denisou.mail.settings'
    _inherit = 'res.config.settings'

    
    recipients = fields.Many2many('res.users','res_users_denisou_settings_rel','denisou_id','user_id','Users')
    
    
    @api.multi
    def get_recipients(self):
        res = {}
        recipients = self.env['ir.config_parameter'].get_param('denisou_mail.recipients')
        
        res['recipients'] = recipients
        
        return res
    
    @api.multi
    def get_default_recipients(self):
        res = {}
        recipients = safe_eval(self.env['ir.config_parameter'].get_param('denisou_mail.recipients','False'))
        if recipients:
            res.update({'recipients':recipients})
        #test = self.payment_term_partner
        
        return res
    
    @api.multi
    def set_recipients(self):
        
        self.env['ir.config_parameter'].set_param('denisou_mail.recipients',repr(self.recipients.mapped('id')))
    '''    
    @api.multi
    def get_default_payment_term_customer(self):
        res = {}
        term = safe_eval(self.env['ir.config_parameter'].get_param('default_payment_term.payment_term_customer','False'))
        if term:
            res.update({'payment_term_customer':term})
        #test = self.payment_term_partner
        
        return res
    '''
    '''
    @api.multi
    def set_payment_term_customer(self):
        
        self.env['ir.config_parameter'].set_param('default_payment_term.payment_term_customer',repr(self.payment_term_customer.id))
    '''  

res_config()