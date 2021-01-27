from odoo import models, fields, api
from odoo.exceptions import ValidationError


class registro_model(models.Model):
    _name = 'cooperativa.registro_model'
    _description = 'Modelo de Registros'

    id_socio = fields.Many2one("cooperativa.socio_model", "Socio")
    id_campanya = fields.Many2one("cooperativa.campanya_model", "Campanya")
    id_producto = fields.Many2one("cooperativa.producto_model", "Producto")
    cantidad = fields.Integer(string="Cantidad")

    @api.constrains("cantidad")
    def _cantidadMayor0(self):
        if self.cantidad <= 0:
            raise ValidationError("La cantidad debe de ser mayor de 0")
