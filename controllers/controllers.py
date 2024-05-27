# -*- coding: utf-8 -*-
from odoo import http


class Concesionari(http.Controller):
    @http.route('/concesionari/concesionari', auth='public')
    def index(self, **kw):
        return "Hello, world"
    @http.route('/concesionari/concesionari/objects', auth='public')
    def list(self, **kw):
        return http.request.render('concesionari.listing', {
            'root': '/concesionari/concesionari',
            'objects': http.request.env['concesionari.concesionari'].search([]),
        })
    @http.route('/concesionari/concesionari/objects/<model("concesionari.concesionari"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('concesionari.object', {
            'object': obj
        })