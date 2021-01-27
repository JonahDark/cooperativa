from odoo import models, fields, api
from datetime import datetime


class campanya_model(models.Model):
    _name = 'cooperativa.campanya_model'
    _description = 'Modelo de Campanya'

    fecha = fields.Date(
        string="Fecha", default=datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    campanya = fields.Integer(string="Campanya", default=datetime.today().year)
    socio = fields.Many2one("cooperativa.socio_model", "Socio")
    producto = fields.Many2one("cooperativa.producto_model", "Producto")
    kilos = fields.Integer(string="Kilos")
    socio = fields.Many2one("cooperativa.socio_model", "Socio")
    registro_campanya = fields.One2many(
        "cooperativa.registro_model", "id_campanya", "Campanya")

    def actualizaSaldo(self):
        for i in self.registro_campanya:
            i.id_socio.saldo += i.id_producto.precio*i.cantidad

    def eliminaHistorial(self):
        self.ensure_one()
        for i in self.registro_campanya:
            i.unlink()
