# -*- coding: utf-8 -*-

from odoo import models, fields, api

class concesionari(models.Model):
    _name = 'concesionari.concesionari'
    _description = 'concesionari.concesionari'

    # MY FIELDS
    image_concesionari = fields.Binary(string="image")
    name = fields.Char()
    cif = fields.Char()
    address = fields.Char()
    segona_ma = fields.Boolean()
    cars = fields.Integer(compute="_compute_cars", store=True)
    nom_ceo = fields.Char()
    dni = fields.Char()
    description = fields.Text()
    vehicles = fields.One2many(comodel_name="concesionari.cotxe", string="Vehicles", inverse_name="concesionari")

    @api.depends('vehicles')
    def _compute_cars(self):
        for record in self:
            record.cars = len(record.vehicles)
    #value2 = fields.Float(compute="_value_pc", store=True)
    #@api.depends('value')
    #def _value_pc(self):
    #    for record in self:
    #        record.value2 = float(record.value) / 100
    
    
class cotxe(models.Model):
    
    _name = 'concesionari.cotxe'
    _description = 'concesionari.cotxe'
    
    image_cotxe = fields.Binary(string="image")
    marca = fields.Char()
    model = fields.Char()
    preu = fields.Float()
    segona_ma = fields.Boolean()
    description = fields.Text()
    concesionari = fields.Many2one('concesionari.concesionari', 'Concesionari', ondelete="cascade")
