# -*- coding: utf-8 -*-
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


class res_partner_mail(models.Model):
    """ Update partner to add a field about notification preferences """
    _name = "res.partner"
    _inherit = ['res.partner', 'mail.thread']

    notify_email = fields.Selection([
            ('none', 'Never'),
            ('always', 'All Messages'),
            ], 'Receive Inbox Notifications by Email', required=True,
            oldname='notification_email_send',
            default= lambda *args: 'none',
            help="Policy to receive emails for new messages pushed to your personal Inbox:\n"
                    "- Never: no emails are sent\n"
                    "- All Messages: for every notification you receive in your Inbox")

res_partner_mail()