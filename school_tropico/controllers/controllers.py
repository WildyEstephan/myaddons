# -*- coding: utf-8 -*-
from odoo import http

# class SchoolTropico(http.Controller):
#     @http.route('/school_tropico/school_tropico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_tropico/school_tropico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_tropico.listing', {
#             'root': '/school_tropico/school_tropico',
#             'objects': http.request.env['school_tropico.school_tropico'].search([]),
#         })

#     @http.route('/school_tropico/school_tropico/objects/<model("school_tropico.school_tropico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_tropico.object', {
#             'object': obj
#         })