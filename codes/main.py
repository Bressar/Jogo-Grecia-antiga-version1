import random
from random import randint
import time
from movimentos_e_cartas import Tabuleiro, Cards, dic_cards
from casas import Casas
from players import dic_players  # Dicionário de jogadores


def linha(numero):
    print("--" * numero)


class Main:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.cards = Cards()
        self.cartas_player = []
        self.cartas_usadas = []
        self.posicao_atual = 0
        self.__pontos = 0
        self.__vida = 3
        self.nome_player = None
        self.casas = Casas(self.tabuleiro, self.cartas_player)  # Passa cartas_player - Gambiarra!


    def escolher_jogador(self):
        print("CHOOSE A PLAYER".center(70))
        while True:
            escolhido = input("[1] Polyphemus - [2] Hippolyta - [3] Odysseus - [4] Medusa - [5] Chiron ").strip()
            print("<>" * 35)
            player = dic_players.get(escolhido)
            if player:
                print(f"Your player is:\n{player}")
                print("**" * 35)
                self.nome_player = player # salva o nome para uma variável
                self.tabuleiro.nome_player = player  # Update na váriavel na classe tabuleiro
                return player
            else:
                print("Unknow player, choose again!")
                print("**" * 35)


    def iniciar_jogo(self):
        print("<>" * 35)
        print("ASCENT to OlYMPUS".center(70))
        print("The ancient greekg game".center(70))
        print("<>" * 35)
        jogador = self.escolher_jogador()
        if not jogador:
            return

        time.sleep(2)
        self.tabuleiro.escolher_carta()  # Chamar a função escolher_carta e passar a instância de Tabuleiro

        time.sleep(2)
        while True:
            resposta = input('Press:\n[C] Use a card\n[D] Roll one die\n[X] To Exit ').strip().upper()
            linha(35)
            if resposta == 'C': # função usar carta
                self.tabuleiro.usar_carta()
            elif resposta == 'D':
                numero_sorteado = self.tabuleiro.rolar_dado()
                if not self.tabuleiro.atualizar_posicao(numero_sorteado):
                    break
                self.tabuleiro.exibir_estado(numero_sorteado)

                # Aqui começam os eventos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if self.tabuleiro.posicao_atual == 1:
                   self.casas.casa001()

                elif self.tabuleiro.posicao_atual == 2:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 4:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 5:
                    self.casas.casa005()

                elif self.tabuleiro.posicao_atual == 6:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 8:
                    self.casas.casa008()

                elif self.tabuleiro.posicao_atual == 9:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 10:
                    self.casas.casa010()

                elif self.tabuleiro.posicao_atual == 11:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 13:
                    self.casas.casa013()

                elif self.tabuleiro.posicao_atual == 15:
                   self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 17:
                    self.casas.casa017()

                elif self.tabuleiro.posicao_atual == 19:
                   self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 21:
                    self.casas.casa021()

                elif self.tabuleiro.posicao_atual == 22:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 24:
                    self.casas.casa024()

                elif self.tabuleiro.posicao_atual == 25:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 28:
                    self.casas.casa028()

                elif self.tabuleiro.posicao_atual == 30:
                    self.casas.casa030()

                elif self.tabuleiro.posicao_atual == 31:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 32:
                    self.casas.casa032()

                elif self.tabuleiro.posicao_atual == 34:
                    self.casas.casa034()

                elif self.tabuleiro.posicao_atual == 36:
                    self.casas.casa036()

                elif self.tabuleiro.posicao_atual == 38:
                    self.casas.casa038()

                elif self.tabuleiro.posicao_atual == 39:
                    self.casas.casa039()

                elif self.tabuleiro.posicao_atual == 41:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 42:
                    self.casas.casa042()

                elif self.tabuleiro.posicao_atual == 44:
                    self.casas.casa044()

                elif self.tabuleiro.posicao_atual == 46:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 48:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 49:
                    self.casas.casa049()

                elif self.tabuleiro.posicao_atual == 51:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 52:
                    self.casas.casa052()

                elif self.tabuleiro.posicao_atual == 55:
                    self.casas.casa055()

                elif self.tabuleiro.posicao_atual == 58:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 60:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 61:
                    self.casas.casa061()

                elif self.tabuleiro.posicao_atual == 62:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 64:
                    self.casas.casa064()

                elif self.tabuleiro.posicao_atual == 65:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 66:
                    self.casas.casa066()

                elif self.tabuleiro.posicao_atual == 69:
                    self.casas.casa069()

                elif self.tabuleiro.posicao_atual == 71:
                    self.casas.casa071()

                elif self.tabuleiro.posicao_atual == 73:
                    self.casas.casa073()

                elif self.tabuleiro.posicao_atual == 74:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 75:
                    self.casas.casa075()

                elif self.tabuleiro.posicao_atual == 76:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 79:
                    self.casas.casa079()

                elif self.tabuleiro.posicao_atual == 81:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 82:
                    self.casas.casa082()

                elif self.tabuleiro.posicao_atual == 83:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 84:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 85:
                    self.casas.casa085()

                elif self.tabuleiro.posicao_atual == 86:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 88:
                    self.casas.casa088()

                elif self.tabuleiro.posicao_atual == 89:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 90:
                    self.casas.casa090()

                elif self.tabuleiro.posicao_atual == 92:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 93:
                    self.casas.casa093()

                elif self.tabuleiro.posicao_atual == 94:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 95:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 96:
                    self.casas.casa096()

                elif self.tabuleiro.posicao_atual == 97:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 98:
                    self.casas.casa098()

                elif self.tabuleiro.posicao_atual == 100:
                    self.casas.casa100()

                elif self.tabuleiro.posicao_atual == 101:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 102:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 103:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 104:
                    self.casas.casa104()

                elif self.tabuleiro.posicao_atual == 106:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 107:
                    self.casas.casa107()

                elif self.tabuleiro.posicao_atual == 108:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 110:
                    self.casas.casa110()

                elif self.tabuleiro.posicao_atual == 112:
                    self.casas.casa112()

                elif self.tabuleiro.posicao_atual == 113:
                    self.casas.volta_casa()

                elif self.tabuleiro.posicao_atual == 114:
                    self.casas.avanca_casa()

                elif self.tabuleiro.posicao_atual == 115:
                   self.casas.retorna_avanca()

                elif self.tabuleiro.posicao_atual == 116:
                    self.casas.casa116()

                elif self.tabuleiro.posicao_atual == 119:
                    self.casas.casa116()

                elif self.tabuleiro.posicao_atual > 120:
                    print("""You have won!"
"Now you can ask the Gods for your boon!"
"They will grant it to you, or maybe not, who knows? "
"The Greek Gods are temperamental...""")
                    linha(35)

                time.sleep(1)
                # self.tabuleiro.exibir_cartas()  # Exibir cartas do jogador a cada rodada
                linha(35)
                self.casas.posicao_casas()
                print(f"Points: {self.tabuleiro.pontos_posicao_tabuleiro()}")
                print(f"XP: {self.tabuleiro.vida}")
                linha(35)
                if self.tabuleiro.vida <= 0:
                    print("You have lost all your lives. Game over!")
                    break
            elif resposta == 'X':
                print('See you next time! Exiting program...')
                print(">>" * 35)
                break
            else:
                print('Invalid value, please choose again.')

if __name__ == "__main__":
    main = Main()
    main.iniciar_jogo()
