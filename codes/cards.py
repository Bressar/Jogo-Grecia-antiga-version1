from tabuleiro import Tabuleiro
import random

class Cards:
    def __init__(self, nome=None, action=None, image=None):
        self.nome = nome
        self.action = action
        self.image = image


    def __str__(self):
        return f"{self.nome}, {self.action}"



athena = Cards("Athena", "Win 1 battle, or advance 2 spaces", image=None)
ares = Cards("Ares", "Win 1 battle, or roll 1 die", image=None)
hades = Cards("Hades",  "Gain one life", image=None)
hermes = Cards("Hermes",  "Advance 5 spaces, or skip 1 space", image=None)
poseidon = Cards("Poseidon",  "Advance 4 spaces, or roll 1 die", image=None)
hera = Cards("Hera",  "Gain one life, or roll 1 die", image=None)
zeus = Cards("Zeus", "Advance 6 spaces, or roll 2 dice", image=None)
persephone = Cards("Persephone",  "Go back 1, 2, or 3 spaces", image=None)
hephaestus = Cards("Hephaestus", "Roll 1 die again", image=None)
aphrodite = Cards("Aphrodite", "Advance 6 spaces", image=None)
apollo = Cards("Apollo", "Roll 2 dice", image=None)
artemis = Cards("Artemis",  "Advance 3 spaces, or roll 1 die", image=None)

dic_cards = {
    "1": athena,
    "2": ares,
    "3": hades,
    "4": hermes,
    "5": poseidon,
    "6": hera,
    "7": persephone,
    "8": hephaestus,
    "9": aphrodite,
    "11": apollo,
    "12": artemis
}


def executar_acao(self, tabuleiro):
    raise NotImplementedError("Ação deve ser implementada nas subclasses")


class Athena(Cards):
    def executar_acao(self, tabuleiro):
        print("Athena: Win 1 battle, or advance 2 spaces.")
        escolha = input("Escolha 'B' para batalha ou 'A' para avançar 2 casas: ").upper().strip()
        if escolha == 'B':
            dado_rolagem = input("Role 1 dado[D]").upper().strip()
            if escolha == "D":
                resultado = randint(1, 6)
                if resultado >= 4:
                    print("Você ganhou uma batalha!")
                    tabuleiro.atualizar_posicao(2)
                    tabuleiro.pontos += 50
                else:
                    tabuleiro.vida -= 1
                    tabuleiro.pontos -= 45
                    print(f"Você perdeu uma vida, ainda lhe restam {tabuleiro.vida}")
        elif escolha == 'A':
            tabuleiro.atualizar_posicao(2)
            print("Você avançou 2 casas!")
        else:
            print('Escolha inválida!')


