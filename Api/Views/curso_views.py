from flask_restful import Resource
from Api import api
from ..Schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..Services import curso_service, formacao_service
from ..paginate import paginate
from ..models.curso_model import Curso


class CursoList(Resource):
	def get(self):
		cs = curso_schema.CursoSchema(many=True)
		return paginate(Curso, cs)
  
	def post(self):
		cs = curso_schema.CursoSchema()  
		validate = cs.validate(request.json)
		if validate:
			return make_response(jsonify(validate), 400) 
		else:
			nome = request.json['nome']
			descricao = request.json['descricao']
			data_publicacao = request.json['data_publicacao']
			formacao = request.json['formacao']
			formacao_curso = formacao_service.listar_formacao_id(formacao)
			if formacao_curso is None:
				return make_response(jsonify("Formação não foi encontrada"), 404)
            

			novo_curso = curso.Curso(nome=nome,
                        descricao=descricao,
                        data_publicacao=data_publicacao,
                        formacao=formacao_curso)
   
			resultado = curso_service.cadastrar_curso(novo_curso)
			x = cs.jsonify(resultado)
			return make_response(x, 201)




class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não foi encontrado!"), 404)
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify("Curso não foi encontrado!"), 404)

        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']
            formacao = request.json['formacao']
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("Formação não foi encontrada"), 404)
            
            novo_curso = curso.Curso(
                nome=nome, 
                descricao=descricao, 
                data_publicacao=data_publicacao,
                formacao=formacao_curso,  
            )
            curso_service.atualiza_curso(curso_bd, novo_curso)
            curso_atualizado = curso_service.listar_curso_id(id)
            
            return make_response(cs.jsonify(curso_atualizado), 200)


    def delete(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify("Curso não foi encontrado!"), 404)
        curso_service.remove_curso(curso_bd)
        return make_response(jsonify("Curso deletado com sucesso!"), 200)    
           

    
api.add_resource(CursoList,'/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')