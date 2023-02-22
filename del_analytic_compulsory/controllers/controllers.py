# -*- coding: utf-8 -*-
# from odoo import http


# class DelAnalyticCompulsory(http.Controller):
#     @http.route('/del_analytic_compulsory/del_analytic_compulsory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/del_analytic_compulsory/del_analytic_compulsory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('del_analytic_compulsory.listing', {
#             'root': '/del_analytic_compulsory/del_analytic_compulsory',
#             'objects': http.request.env['del_analytic_compulsory.del_analytic_compulsory'].search([]),
#         })

#     @http.route('/del_analytic_compulsory/del_analytic_compulsory/objects/<model("del_analytic_compulsory.del_analytic_compulsory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('del_analytic_compulsory.object', {
#             'object': obj
#         })
