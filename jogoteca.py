# We need to import request, redirect, and url_for from Flask
from flask import Flask, render_template, request, redirect, url_for

# The Jogo class remains the same
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# Initial list of games
jogo1 = Jogo('God of War', 'Ação', 'PS4')
jogo2 = Jogo('Skyrim', 'RPG', 'PC')
jogo3 = Jogo('Valorant', 'FPS', 'PC')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def listar_jogos():
    return render_template('lista.html', titulo='Jogoteca', jogos=lista)

@app.route('/novo')
def novo_jogo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    novo_jogo_obj = Jogo(nome, categoria, console)
    lista.append(novo_jogo_obj)
    
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
