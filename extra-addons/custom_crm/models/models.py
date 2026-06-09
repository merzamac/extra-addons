# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'custom_crm.visit'

    name = fields.Char(string="Descripcion")
    costumer = fields.Char(string="Cliente")
    date = fields.Datetime(string="Fecha")
    type = fields.Selection([('P','Personal'),('W','Whatsapp'),('T','Telefono')],string="Tipo", required=True)
    done = fields.Boolean(string="Realizado", readonly=True)

