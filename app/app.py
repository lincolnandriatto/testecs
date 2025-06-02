# docker image build -t api-py3.1 . 
# docker container run -p 80:80 --name api-py-3.1 api-py3.1 
# docker container start api-py-3.1

# from flask import Flask
from flask import Flask, jsonify, request
app = Flask(__name__)

tarefas = [ {'id': 0, 'descricao': "default"} ]
@app.route('/')
def home():
    return 'Bem-vindo à API de tarefas!'
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    descricao = request.json.get('descricao')
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao}
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)