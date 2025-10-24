# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Presupuesto(models.Model):
    _name = "presupuesto"
    _inherit =  ['image.mixin']
    name = fields.Char(string='Pelicula')
    clasificacion = fields.Selection(
        selection=[
            ("G", "G"), #Publico gemeral
            ("PG", "PG"), #Se recomienda la compania de un adulto
            ("PG-13", "PG-13"), #Mayoes de 13
            ("R", "R"), #Mayores de 18
        ], string="Clasificacion")
    fch_estreno = fields.Date(string='Fecha estreno')
    puntuacion = fields.Integer(string='Puntuacion', related="puntuacion2")
    puntuacion2 = fields.Integer(string='Puntuacion2')
    active = fields.Boolean(string='Activo', default=True)
    director_id = fields.Many2one(
        comodel_name='res.partner',
        string='Director'
    )
    genero_ids = fields.Many2many(
        comodel_name='genero',
        string='Generos'
    )
    vista_general = fields.Text(string='Descripcion')