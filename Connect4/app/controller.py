from flask import Flask, render_template, request, jsonify
import pygame
from model import Tabuleiro
from view import CaixaTexto
from constants import BRANCO, PRETO, LARGURA, ALTURA, TAMANHO_CELULA, VERMELHO

app = Flask(__name__)

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Connect 4")

        self.jogador_atual = 1

        self.fonte = pygame.font.Font(None, 36)

        self.caixa_texto_jogador = CaixaTexto(100, 100, 200, 40, BRANCO, PRETO, self.fonte, PRETO)

        self.nome_jogador1 = ""
        self.nome_jogador2 = ""

        self.tabuleiro = Tabuleiro()

jogo = GameController()

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit_name', methods=['POST'])
def submit_name():
    jogador_atual = request.form['jogador_atual']
    nome_jogador = request.form['nome_jogador']
    
    if jogador_atual == '1':
        jogo.nome_jogador1 = nome_jogador
    elif jogador_atual == '2':
        jogo.nome_jogador2 = nome_jogador

    if jogo.nome_jogador1 and jogo.nome_jogador2:
        return jsonify({'status': 'success', 'jogador_atual': 1})
    else:
        return jsonify({'status': 'wait', 'jogador_atual': int(jogador_atual) + 1})


@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    coluna = int(request.form['coluna'])
    jogador_atual = int(request.form['jogador_atual'])

    if jogo.tabuleiro.fazer_movimento(coluna, jogador_atual):
        if jogo.tabuleiro.verificar_vencedor():
            return jsonify({'status': 'winner', 'nome_vencedor': jogo.nome_jogador1 if jogador_atual == 1 else jogo.nome_jogador2})
        else:
            jogo.jogador_atual = 3 - jogador_atual
            return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'invalid_move'})

if __name__ == "__main__":
    app.run(debug=True)
