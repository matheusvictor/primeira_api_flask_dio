import json

from flask import Flask, jsonify, request

app = Flask(__name__)

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


@app.route('/', methods=['GET'])
def index():
    return jsonify(lista_tarefas)


@app.route('/tarefa/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def tarefa(id):
    try:
        response = lista_tarefas[id]

        if request.method == 'DELETE':
            lista_tarefas.pop(id)
            mensagem = f'Tarefa de ID {id} excluída com sucesso!'
            response = {'status': f'{mensagem}'}
        elif request.method == 'PUT':
            status_atualizado = json.loads(request.data)
            lista_tarefas[id]['status'] = status_atualizado['status']
            mensagem = f'Status da tarefa de ID {id} atualizado com sucesso!'
            response = {'status': f'{mensagem}'}

    except IndexError:
        mensagem = f'Não existe tarefa com ID {id} na lista de afazeres.'
        response = {'status': f'{mensagem}'}
    except Exception:
        mensagem = f'Erro desconhecido.'
        response = {'status': f'{mensagem}'}

    return jsonify(response)


@app.route('/cadastrar', methods=['POST'])
def cadastrar_tarefa():
    payload = json.loads(request.data)
    nova_tarefa = {
        'id': len(lista_tarefas) + 1,
        'responsavel': payload['responsavel'],
        'tarefa': payload['tarefa'],
        'status': payload['status']
    }
    return nova_tarefa


if __name__ == '__main__':
    app.run(debug=True)
