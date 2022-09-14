# -*- coding: utf-8 -*-
# from odoo import http


# class Zulmart(http.Controller):
#     @http.route('/zulmart/zulmart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zulmart/zulmart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zulmart.listing', {
#             'root': '/zulmart/zulmart',
#             'objects': http.request.env['zulmart.zulmart'].search([]),
#         })

#     @http.route('/zulmart/zulmart/objects/<model("zulmart.zulmart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zulmart.object', {
#             'object': obj
#         })
