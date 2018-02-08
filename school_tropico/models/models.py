# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Seccion(models.Model):
    _name = 'seccion.tropico'
    _description = 'Secciones'

    name = fields.Char(string='Nombre seccion', required=True)
    sequence = fields.Integer(string="Secuencia", required=False, )


class Nivel(models.Model):
    _name = 'grade.tropico'
    _description = 'Niveles'

    name = fields.Char(string='Nombre de nivel', help='Ejempo: 1ro Bachiller', required=True)
    secciones_ids = fields.Many2many(comodel_name="seccion.tropico", string="Secciones", )

class Semestre(models.Model):
    _name = 'semestre.tropico'

    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(string="Fecha de inicio", required=False, )
    end_date = fields.Date(string="Fecha Final", required=False, )


class PeriodoEscolar(models.Model):
    _name = 'periodo.tropico'

    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(string="Fecha de inicio", required=False, )
    end_date = fields.Date(string="Fecha Final", required=False, )
    semestres_ids = fields.Many2many(comodel_name="semestre.tropico", string="Semestres", )

class Escuela(models.Model):
    _name = 'escuela.tropico'

    name = fields.Char(string='Nombre escuela', required=True)
    calle1 = fields.Char(string="Calle", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    country_id = fields.Many2one(comodel_name="res.country", string="Pais", required=False, )
    state_id = fields.Many2one(comodel_name="res.country.state", string="Provincia", required=False, )
    niveles_ids = fields.Many2many(comodel_name="grade.tropico", string="Niveles", )

class Padres(models.Model):
    _name = 'padres.tropico'

    nombre = fields.Char(string="Nombre", required=True, )
    telefono = fields.Char(string="Telefono", required=False, )
    movil = fields.Char(string="Movil", required=False, )
    email = fields.Char(string="Email", required=False, )
    calle1 = fields.Char(string="Calle", required=False, )
    ciudad = fields.Char(string="Ciudad", required=False, )
    country_id = fields.Many2one(comodel_name="res.country", string="Pais", required=False, )
    notas = fields.Text(string="Notas", required=False, )

class Estudiante(models.Model):
    _inherit = 'res.partner'

    matricula = fields.Char(string="Matricula", required=False, )
    numero_orden = fields.Integer(string="Numero de orden", required=False, )
    year_id = fields.Many2one(comodel_name="periodo.tropico", string="Periodo Escolar", required=False, )
    escuela_id = fields.Many2one(comodel_name="escuela.tropico", string="Escuela", required=False, )
    grado_id = fields.Many2one(comodel_name="grade.tropico", string="Nivel", required=False, )
    seccion_id = fields.Many2one(comodel_name="seccion.tropico", string="Seccion", required=False, )
    birth_day = fields.Date(string="Fecha de nacimiento", required=False, )
    admission_date = fields.Date(string="Fecha de admision", required=False, )
    sexo = fields.Selection(string="Sexo", selection=[('1', 'Mujer'), ('2', 'Hombre'), ], required=False, )
    padres_ids = fields.Many2many(comodel_name="padres.tropico", string="Padres", )
