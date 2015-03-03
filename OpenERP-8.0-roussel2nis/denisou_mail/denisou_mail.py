from openerp.osv import osv,fields
from datetime import datetime, timedelta
from openerp.tools.safe_eval import safe_eval
from openerp import SUPERUSER_ID


class res_users(osv.osv):
    _inherit='res.users'
    _columns={
              'receive_notifications':fields.boolean(string="Receive Notifications")
              }

class denisou_mail(osv.osv):
    _name="denisou.mail"
    def send_supplier_due_invoice(self,cr,uid,context=None):
        
        ids = self.pool.get('account.invoice').search(cr,uid,[('type','=','in_invoice'),('date_due','<=',datetime.now()-timedelta(days=2)),('date_due','>',datetime.now()-timedelta(days=60)),('reconciled','=',False)])
        
        invoices = self.pool.get('account.invoice').browse(cr,uid,ids,context)
        
        body="Invoices that are awaiting payments :<br/><br/>"
        
        body+='<table style="border:1px solid black">'
        body+='<tr style="border:1px solid black">'
        body+="<td>Partner</td>"
        body+="<td>Invoice Number</td>"
        body+="<td>Due Date</td>"
        body+="<td>Amount</td>"
        body+="</tr>"
        
        for invoice in invoices:
            body+='<tr style="border:1px solid black">'
            body+="<td>"+invoice.partner_id.name+"</td>"
            body+="<td>"+invoice.number+"</td>"
            body+="<td>"+invoice.date_due+"</td>"
            body+="<td>"+str(invoice.amount_total)+"</td>"
            body+="</tr>"
      
            
        
        message = self.pool.get('mail.mail')
        email_to=[]
        recipients = safe_eval(self.pool.get('ir.config_parameter').get_param(cr,SUPERUSER_ID,'denisou_mail.recipients','False'))
        for user in self.pool.get('res.users').browse(cr,uid,recipients,context=context):
            if user.email:
                msg_vals = {
                    'subject':'[DenIsou] Invoices awaiting payment',
                    'body_html':body,
                    'email_from':'roussel2nis@gmail.com',
                    'email_to':user.email,
                    
                    }
                msg_id=message.create(cr,uid,msg_vals,context)
                if msg_id:
                    message.send(cr,uid,[msg_id],context=context)
        return True