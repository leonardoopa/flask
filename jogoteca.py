from flask import Flask, render_template

class Jogo:
    def __init__(self,nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console




app = Flask(__name__)

@app.route('/inicio')
def ola_mundo():

    jogo1 = Jogo('God of War', 'Ação', 'PS4')
    jogo2 = Jogo('Skyrim', 'RPG', 'PC')
    jogo3 = Jogo('Valorant', 'FPS', 'PC')

    lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogoteca', jogos=lista)


if __name__ == '__main__':
    app.run()