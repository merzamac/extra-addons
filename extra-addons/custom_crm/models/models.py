# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'custom_crm.visit'

    name = fields.Char(string="Descripcion")
    costumer = fields.Many2one(string="Cliente",comodel_name='res.partner')
    date = fields.Datetime(string="Fecha")
    type = fields.Selection([('P','Personal'),('W','Whatsapp'),('T','Telefono')],string="Tipo", required=True)
    done = fields.Boolean(string="Realizado", readonly=True)
    image = fields.Binary(string="Imagen")

    def toggle_state(self):
        self.done = not self.done

    def f_create(self):
        visit={
            'name': 'ORM test',
            'costumer': 1,
            'date': str(datetime.date(2026,1,1)),
            'type':'P',
            'done': False
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit)
    def f_search_update(self):
        visit=self.env['custom_crm.visit'].search([('name','=','ORM test')])

        print('search()',visit,visit.name)

        visit=self.env['custom_crm.visit'].browse([3])

        print('Browse()',visit,visit.name)
        visit.write({
            'name':'ORM test write',
        })

    def f_delete(self):
        visit = self.env['custom_crm.visit'].browse([3])
        #visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        visit.unlink()

class VisitRecord(models.AbstractModel):
    _name = 'report.custom_crm.report_visit_card' # mismo valor de name que esta en template report

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    zone = fields.Selection([('N','Norte'),('C','Center'),('S','Sur')], string="Zona Comercial")