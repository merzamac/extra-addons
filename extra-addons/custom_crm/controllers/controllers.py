# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class VisitController(http.Controller):
    @http.route('/api/visits',auth="public", methods=['GET'], csrf=False)
    def get_visits(self,**kwargs):
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read(
                [],
                ['id','costumer','name','done'],
            )
            response = json.dumps(visits,ensure_ascii=False).encode('utf-8')
            return Response(response, content_type='application/json; charset=utf-8',status=200)
        except Exception as e:
            return  Response(json.dumps({'error': str(e)}),content_type='application/json; charset=utf-8',status=505)

