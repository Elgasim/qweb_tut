from odoo import http
from odoo.http import request

class QwebTutorials(http.Controller):
    @http.route('/qweb-tutorials',type='http',auth='public',website=True)
    def qweb_tut(self):
        data = {}
        return request.render('qweb_tut.somePythonTemplate',data)
