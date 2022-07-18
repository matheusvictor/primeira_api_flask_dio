import json

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

lista_tarefas = [
    {
        'id': 0,
        'responsavel': 'Matheus',
        'tarefa': 'Estudar Flask',
        'status': 'Afazer'
    },
    {
        'id': 1,
        'responsavel': 'Matheus',
        'tarefa': 'Estudar Flask',
        'status': 'Afazer'
    }
]


class ListaTarefas(Resource):
    def get(self):
        return lista_tarefas


class Tarefas(Resource):
    def get(self, id):
        try:
            response = lista_tarefas[id]
        except IndexError:
            mensagem = f'Não existe tarefa com ID {id} na lista de afazeres.'
            response = {'status': f'{mensagem}'}
        except Exception:
            mensagem = f'Erro desconhecido.'
            response = {'status': f'{mensagem}'}
        return response

    def put(self, id):
        status_atualizado = json.loads(request.data)
        lista_tarefas[id]['status'] = status_atualizado['status']
        mensagem = f'Status da tarefa de ID {id} atualizado com sucesso!'
        response = {'status': f'{mensagem}'}
        return response

    def delete(self, id):
        lista_tarefas.pop(id)
        mensagem = f'Tarefa de ID {id} excluída com sucesso!'
        response = {'status': f'{mensagem}'}
        return response


api.add_resource(ListaTarefas, '/')  # rota para listagem de todas as tarefas
api.add_resource(Tarefas, '/tarefa/<int:id>')  # rota para listagem de tarefas

if __name__ == '__main__':
    app.run(debug=True)
