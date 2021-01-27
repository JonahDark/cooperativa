from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class socio_model(models.Model):
    _name = 'cooperativa.socio_model'
    _description = 'Modelo de Socio'
    _sql_constraints=[("cooperativa_unique_dni","UNIQUE(dni)","Este DNI ya existe"),]
    _sql_constraints=[("cooperativa_unique_idSocio","UNIQUE(name)","Este ID ya existe"),]

    name = fields.Char(string="ID", index=True, required=True)
    foto = fields.Binary(string="Foto")
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    fechaAlta = fields.Date(string="Fecha alta", required=True, default=datetime.today())
    telefono = fields.Char(string="Telefono", required=True)
    email = fields.Char(string="Email")
    saldo = fields.Integer(string="Saldo",default=0)
    campanyas = fields.One2many("cooperativa.campanya_model","socio","Campanyas")

    registro_socio = fields.One2many(
        "cooperativa.registro_model", "id_socio", "Socio")

    @api.constrains('dni')
    def _validarDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        posi = int(num) % 23
        if letra != letras[posi]:
            raise ValidationError("DNI no valido")
        if len(self.dni) > 9:
            raise ValidationError("El DNI no puede ser mayor de 9 caracteres")
        if letra.isnumeric():
            raise ValidationError("El DNI debe terminar con una letra")

    @api.constrains('telefono')
    def _validarTelefono(self):
        if len(self.telefono)>9 or len(self.telefono)<9:
            raise ValidationError("El telefono debe contener 9 digitos")        

    @api.constrains('email')
    def _validarEmail(self):
        if '@' not in self.email:
            raise ValidationError("El email debe contener un @")
        if '.' not in self.email:
            raise ValidationError("El email debe contener un .")