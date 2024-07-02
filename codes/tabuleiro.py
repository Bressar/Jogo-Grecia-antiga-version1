from random import randint
import random
import time

class Tabuleiro:
    def __init__(self):
        self._numeros_tabuleiro = list(range(126))
        self.posicao_atual = 0
        self.pontos = 0
        self.vida = 9
        self.nome = None
        self.casa = 0
        self.texto = None
        self.image = None
        self.cartas_player = []
        self.cartas_usadas = []

    def rolar_dado(self):
        return randint(1, 6)

    def linha(self):
        print("--" * 20)

    def atualizar_posicao(self, numero_sorteado):
        self.posicao_atual += numero_sorteado
        if self.posicao_atual >= len(self._numeros_tabuleiro):
            self.posicao_atual = len(self._numeros_tabuleiro) - 1
            print("Você alcançou o fim do tabuleiro!")
            return False
        return True

    def obter_numeros_exibidos(self):
        inicio = max(self.posicao_atual - 2, 0)
        fim = min(self.posicao_atual + 4, len(self._numeros_tabuleiro))
        return self._numeros_tabuleiro[inicio:fim]

    def exibir_estado(self, numero_sorteado):
        print(f'Número sorteado: {numero_sorteado}')
        time.sleep(1)
        print(f'Você está na casa: {self.posicao_atual}')
        time.sleep(1)
        print(f'Posições do tabuleiro: {self.obter_numeros_exibidos()}')
        time.sleep(1)

    def pontos_posicao_tabuleiro(self):
        self.pontos = self.posicao_atual * 15
        return self.pontos


    def exibir_cartas(self):
        print('--' * 22)
        print("Cartas do jogador:")
        for carta in self.cartas_player:
            print(f'{carta._Cards__nome} -> {carta._Cards__action}')
        print('--' * 22)




