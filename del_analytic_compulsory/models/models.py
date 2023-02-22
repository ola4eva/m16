
from odoo import models, fields, api

class resusers(models.Model):
    _inherit = 'res.users'
    account_analytic_id = fields.Many2one('account.analytic.account',
                                          store=True, string='Analytic Account',
                                        readonly=False, required=False)



class SalesOrder(models.Model):
    _inherit = 'sale.order'
    analytic_account_id = fields.Many2one(
        'account.analytic.account', 'Analytic Account',
        readonly=True, copy=False, check_company=True,  # Unrequired company
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="The analytic account related to a sales order.",required=False,default=lambda self:self.env.user.account_analytic_id.id)





class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    account_analytic_id = fields.Many2one('account.analytic.account', store=True, string='Analytic Account',
                                          compute='_compute_account_analytic_id', readonly=False,required=True)

class Hrexpense(models.Model):
    _name = 'hr.expense'
    _inherit = 'hr.expense'
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', check_company=True,required=True,
                                          default=lambda self:self.env.user.account_analytic_id.id)

