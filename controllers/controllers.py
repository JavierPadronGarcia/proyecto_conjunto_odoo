# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoJavier(http.Controller):
#     @http.route('/proyecto_javier/proyecto_javier', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_javier/proyecto_javier/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_javier.listing', {
#             'root': '/proyecto_javier/proyecto_javier',
#             'objects': http.request.env['proyecto_javier.proyecto_javier'].search([]),
#         })

#     @http.route('/proyecto_javier/proyecto_javier/objects/<model("proyecto_javier.proyecto_javier"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_javier.object', {
#             'object': obj
#         })
