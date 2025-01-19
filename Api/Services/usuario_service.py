from ..models import usuario_model
from Api import db


def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_bd.encryptar_senha(senha=usuario.senha)
    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd