from odoo import models, fields, api
from odoo.exceptions import ValidationError


class producto_model(models.Model):
    _name = 'cooperativa.producto_model'
    _description = 'Modelo de Producto'
    _sql_constraints = [("cooperativa_unique_producto",
                         "UNIQUE(name)", "Este producto ya existe"), ]

    name = fields.Char(string="Nombre", index=True, required=True)
    descripcion = fields.Html(string="Descripcion", required=True)
    precio = fields.Integer(string="Precio", required=True)
    kilosTotales = fields.Integer(
        string="Kilos", default=0, compute="_kilosTotales")

    registro_producto = fields.One2many(
        "cooperativa.registro_model", "id_producto", "Producto")

    @api.constrains("precio")
    def _precioNoNegativo(self):
        if self.precio < 0:
            raise ValidationError("El precio no puede ser menor que 0")

    def eliminaKilos(self):
        self.kilosTotales = 0

    @api.depends("registro_producto")
    def _kilosTotales(self):
        for i in self.registro_producto.id_campanya:
            self.kilosTotales += i.kilos
