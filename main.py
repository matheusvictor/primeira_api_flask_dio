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


@app.route('/tarefa/<int:id>', methods=['GET'])
def listar_tarefa(id):
    try:
        response = lista_tarefas[id]
        return jsonify(response)
    except IndexError:
        mensagem = f'Não existe tarefa com ID {id} na lista de afazeres.'
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


@app.route('/atualizar_status/<int:id>', methods=['PUT'])
def atualizar_status(id):
    status_atualizado = json.loads(request.data)
    lista_tarefas[id]['status'] = status_atualizado['status']
    return jsonify(lista_tarefas[id])


@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):

    try:
        response = lista_tarefas[id]
        mensagem = f'Tarefa de ID {id} excluída com sucesso.'
        response = {'status': f'{mensagem}'}

    except IndexError:
        mensagem = f'Não existe tarefa com ID {id} na lista de afazeres.'
        response = {'status': f'{mensagem}'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
