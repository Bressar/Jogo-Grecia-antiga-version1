from random import randint
import random
import time
from players import dic_players  # Dicionário de jogadores

class Cards:
    def __init__(self, nome=None, action=None, image=None):
        self.nome = nome
        self.action = action
        self.image = image


    def __str__(self):
        return f"{self.nome}, {self.action}"


    def executar_acao(self, tabuleiro):
        raise NotImplementedError("Ação deve ser implementada nas subclasses")


    def linha_cards(self, number):
        print('##' * number)


# Classes das cartas cada uma com as suas ações especificas:

class Athena(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Athena: Win 1 battle, or advance 2 spaces.")
        while True:
            escolha = input("Press: [B] to battle or [M] to move 2 spaces: ").upper().strip()
            if escolha == 'B':
                        print("You won a battle! + 50 points!")
                        tabuleiro.atualizar_posicao(1)
                        tabuleiro.pontos += 50
                        break
            elif escolha == 'M':
                tabuleiro.atualizar_posicao(2)
                print("Moved 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Ares(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Ares: Win 1 battle, or roll 1 die.")
        while True:
            escolha = input("Choose [B] to battle or [D] to roll 1 die: ").upper().strip()
            if escolha == 'B':
                print("You won a battle!")
                tabuleiro.atualizar_posicao(1)
                tabuleiro.pontos += 50
                break
            elif escolha == 'D':
                resultado = tabuleiro.rolar_dado()
                print(f"Dice roll result: {resultado}")
                tabuleiro.atualizar_posicao(resultado)
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Hades(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Hades: Gain one life.")
        tabuleiro.vida += 1
        print(f"You gained a life, now you have: {tabuleiro.vida} lives")
        self.linha_cards(35)


class Hermes(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Hermes: Advance 5 spaces, or gain 300 points!")
        while True:
            escolha = input("Choose [M] to move 5 spaces or [P] to gain 300 points: ").upper().strip()
            if escolha == 'M':
                tabuleiro.atualizar_posicao(5)
                print("You moved 5 spaces!")
                break
            elif escolha == 'P':
                tabuleiro.pontos += 300
                print("You gained 300 points!")
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Poseidon(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Poseidon: Advance 4 spaces, or roll 1 die.")
        while True:
            escolha = input("Choose [M] to move 4 spaces or [D] to roll 1 die: ").upper().strip()
            if escolha == 'M':
                tabuleiro.atualizar_posicao(4)
                print("You moved 4 spaces!")
                break
            elif escolha == 'D':
                resultado = tabuleiro.rolar_dado()
                print(f"Dice roll result: {resultado}")
                tabuleiro.atualizar_posicao(resultado)
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Hera(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Hera: Gain one life, or roll 1 die.")
        while True:
            escolha = input("Choose [L] to gain a life or [D] to roll 1 die: ").upper().strip()
            if escolha == 'L':
                tabuleiro.vida += 1
                print(f"You gained a life, now you have: {tabuleiro.vida} lives")
                break
            elif escolha == 'D':
                resultado = tabuleiro.rolar_dado()
                print(f"Dice roll result: {resultado}")
                tabuleiro.atualizar_posicao(resultado)
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Zeus(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Zeus: Advance 6 spaces, or roll 2 dice.")
        while True:
            escolha = input("Choose [M] to move 6 spaces or [D] to roll 2 dice: ").upper().strip()
            if escolha == 'M':
                tabuleiro.atualizar_posicao(6)
                print("You moved 6 spaces!")
                break
            elif escolha == 'D':
                resultado = tabuleiro.rolar_dado() + tabuleiro.rolar_dado()
                print(f"Dice roll result: {resultado}")
                tabuleiro.atualizar_posicao(resultado)
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Persephone(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Persephone: Go back 1, 2, or 3 spaces.")
        while True:
            escolha = input("Choose [1], [2], or [3] to go back that many spaces: ").strip()
            if escolha in ['1', '2', '3']:
                tabuleiro.atualizar_posicao(-int(escolha))
                print(f"You went back {escolha} spaces!")
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Hephaestus(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Hephaestus: Roll 1 die again.")
        while True:
            resultado = tabuleiro.rolar_dado()
            print(f"Você rolou um {resultado}")
            escolha = input("Do you want to roll the dice again? [Y] [N] ").strip().upper()
            if escolha == "Y":
                continue  # Rola o dado novamente no próximo loop
            elif escolha == "N":
                tabuleiro.atualizar_posicao(resultado)
                print(f"Moved {resultado} spaces!")
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


class Aphrodite(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Aphrodite: Advance 6 spaces.")
        tabuleiro.atualizar_posicao(6)
        print("You moved 6 spaces!")
        self.linha_cards(35)


class Apollo(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Apollo: Roll 2 dice.")
        resultado = tabuleiro.rolar_dado() + tabuleiro.rolar_dado()
        print(f"Dice roll result: {resultado}")
        self.linha_cards(35)


class Artemis(Cards):
    def executar_acao(self, tabuleiro):
        self.linha_cards(35)
        print("Artemis: Advance 3 spaces, or roll 1 die.")
        while True:
            escolha = input("Choose [M] to move 3 spaces or [D] to roll 1 die: ").upper().strip()
            if escolha == 'M':
                tabuleiro.atualizar_posicao(3)
                print("You moved 3 spaces!")
                break
            elif escolha == 'D':
                resultado = tabuleiro.rolar_dado()
                tabuleiro.atualizar_posicao(resultado)
                print(f"Dice roll result: {resultado}")
                break
            else:
                print('Invalid choice! Please try again.')
        self.linha_cards(35)


athena = Athena("Athena", "Win 1 battle, or advance 2 spaces", image=None)
ares = Ares("Ares", "Win 1 battle, or roll 1 die", image=None)
hades = Hades("Hades", "Gain one life", image=None)
hermes = Hermes("Hermes", "Advance 5 spaces, or gain 300 points", image=None)
poseidon = Poseidon("Poseidon", "Advance 4 spaces, or roll 1 die", image=None)
hera = Hera("Hera", "Gain one life, or roll 1 die", image=None)
zeus = Zeus("Zeus", "Advance 6 spaces, or roll 2 dice", image=None)
persephone = Persephone("Persephone", "Go back 1, 2, or 3 spaces", image=None)
hephaestus = Hephaestus("Hephaestus", "Roll 1 die again", image=None)
aphrodite = Aphrodite("Aphrodite", "Advance 6 spaces", image=None)
apollo = Apollo("Apollo", "Roll 2 dice", image=None)
artemis = Artemis("Artemis", "Advance 3 spaces, or roll 1 die", image=None)

dic_cards = {
    "1": athena,
    "2": ares,
    "3": hades,
    "4": hermes,
    "5": poseidon,
    "6": hera,
    "7": zeus,
    "8": persephone,
    "9": hephaestus,
    "10": aphrodite,
    "11": apollo,
    "12": artemis
}


# Classe Tabuleiro com a mecânica do movimento do jogo
class Tabuleiro:
    def __init__(self):
        self._numeros_tabuleiro = list(range(120))
        self.posicao_atual = 0
        self.pontos = 0
        self.vida = 3
        self.nome = None
        self.casa = 0
        self.texto = None
        self.image = None
        self.cartas_player = []
        self.cartas_usadas = []
        self.nome_player = None


    def rolar_dado(self):
        return randint(1, 6) # É um dado D-5 de RPG? (melhor 6!!!) not yet... decidir depois...


    def linha(self, valor):
        print("--" * valor)


    def atualizar_posicao(self, numero_sorteado):
        self.posicao_atual += numero_sorteado
        if self.posicao_atual >= len(self._numeros_tabuleiro):
            self.posicao_atual = len(self._numeros_tabuleiro) - 1
            print("You reached the end of the board!")
            return False
        return True
        self.linha(35)

    def obter_numeros_exibidos(self):
        inicio = max(self.posicao_atual - 2, 0)
        fim = min(self.posicao_atual + 4, len(self._numeros_tabuleiro))
        return self._numeros_tabuleiro[inicio:fim]


    def exibir_estado(self, numero_sorteado):
        print(f'"Drawn number: " {numero_sorteado}')
        time.sleep(1)
        print(f'You are on space: {self.posicao_atual}')
        time.sleep(1)
        print(f'Board positions: {self.obter_numeros_exibidos()}')
        time.sleep(1)
        self.linha(35)

    def pontos_posicao_tabuleiro(self):
        self.pontos = self.posicao_atual * 15
        return self.pontos

    def escolher_carta(self):
        while True:
            carta_escolhida = random.choice(list(dic_cards.keys()))
            carta_inicial = dic_cards[carta_escolhida]
            if carta_inicial not in self.cartas_player and carta_inicial not in self.cartas_usadas:
                if len(self.cartas_player) >= 3:
                    self.cartas_player.pop(0)  # Remove o primeiro item se a lista já tiver 3 itens
                self.cartas_player.append(carta_inicial)
                #self.cartas_usadas.append(carta_inicial)#Carta inicial só será adicionada às cartas usadas após seu uso
                print(f"Your starting card is: {carta_inicial.nome}\n"
                      f"And your power is: {carta_inicial.action}")
                print("**" * 35)
                break


    def exibir_cartas(self):
        self.linha(35)
        print("Player's cards:")
        for carta in self.cartas_player:
            print(f'{carta.nome} -> {carta.action}')
        self.linha(35)


    def usar_carta(self):
        if not self.cartas_player:
            print("You have no cards to use.")
            return
        print("Available cards:")
        for idx, carta in enumerate(self.cartas_player):
            print(f"{idx + 1}. {carta.nome} -> {carta.action}")

        while True:
            escolha = input("Choose a card to use [1][2][3] ")
            if escolha.isdigit():
                idx_escolhido = int(escolha) - 1
                if 0 <= idx_escolhido < len(self.cartas_player):
                    carta_escolhida = self.cartas_player.pop(idx_escolhido)
                    print(f"Using card: {carta_escolhida.nome}")
                    carta_escolhida.executar_acao(self)# Correção aplicada aqui
                    self.cartas_usadas.append(carta_escolhida)# Mover a carta para a lista de usadas
                    break
                else:
                    print("Invalid choice!")
            else:
                print("Invalid input!")
        self.linha(35)



