from Api import ma
from ..models import usuario_model
from marshmallow import fields


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario
        load_instance = True
        fields = ('id', 'name', 'email', 'senha')
        
    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    