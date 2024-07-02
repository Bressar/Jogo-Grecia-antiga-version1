from movimentos_e_cartas import Tabuleiro, Cards, dic_cards
from players import dic_players
from random import randint
import time

class Casas:
    def __init__(self, tabuleiro, cartas_player):
        self.tabuleiro = tabuleiro
        self.cartas_player = cartas_player

    def posicao_casas(self):
        time.sleep(2)
        print(f'You are on space: {self.tabuleiro.posicao_atual}')

    # casa 001 -> Hermes
    def casa001(self):
        self.nome = "Hermes"
        self.casa = 1
        self.image = "image/casa_001.jpg"
        self.texto = "Draw a card or move forward 2 spaces"
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card or [M] to advance 2 spaces").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            elif escolha == "M":
                self.tabuleiro.atualizar_posicao(2)
                print("You moved 2 spaces!")
                break
            else:
                print('Valor inválido! Escolha novamente...')


    # casa 005 -> Esfinge
    def casa005(self):  # casa 005 -> Esfinge
        self.nome = "Sphinx"
        self.casa = 5
        self.image = "image/casa_005.jpg"
        self.texto = """She asked you a question.
Solve the riddle and roll a die.
If you get 3 or more, move forward 2 spaces.
If you get 2 or less, move back 2 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to use a card or [D] to roll 1 die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 3:
                    self.tabuleiro.atualizar_posicao(2)
                    self.tabuleiro.pontos += 100
                    print("You solved the riddle and moved forward 2 spaces!")
                else:
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You failed to solve the riddle, lose 1 life and moved back 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 08 -> Prometheus
    def casa008(self):  # casa 08 -> Prometheus
        self.nome = "Prometheus"
        self.casa = 8
        self.image = "image/casa_008.jpg"
        self.texto = """Watch the condemned Titan in his punishment and return 2 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to use a card or [S] to stay here: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must move back 2 spaces.")
                    escolha = "S"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "S":
                self.tabuleiro.atualizar_posicao(-2)
                self.tabuleiro.pontos -= 60
                print("You moved back 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 10 -> Esparta
    def casa010(self):
        self.nome = "Sparta"
        self.casa = 10
        self.image = "image/casa_010.jpg"
        self.texto = """The Spartans don't like strangers!
Fight for your life.
Use a card or roll a die.
If you win, advance 2 spaces.
If you lose, lose 1 life."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to use a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                if resultado >= 4:
                    print("You defeat the Spartans!")
                    self.tabuleiro.pontos += 100
                    self.tabuleiro.atualizar_posicao(2)
                    break
                else:
                    print("You lose!")
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print(f"You lost 1 life, you still have {self.tabuleiro.vida} left.")
                    break
            else:
                print('Invalid choice! Please try again.')


    # casa 013-> Héstia
    def casa013(self):
        self.nome = "Hestia"
        self.casa = 13
        self.image = "image/casa_013.jpg"
        self.texto = """Draw 1 card or assist the Goddess with her hearth and roll 1 die."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [D] to roll a die or [U] To use a card: ").upper().strip()
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "D":
                resultado = randint(1, 6)
                self.tabuleiro.atualizar_posicao(resultado)
                print(f"You moved {resultado} spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 017-> Quimera
    def casa017(self):
        self.nome = "Chimera"
        self.casa = 17
        self.image = "image/casa_013.jpg"
        self.texto = """Roll 1 die and fight against the monster.
If you lose, move back 3 spaces.
If you win, move forward 3 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You won the fight!")
                    self.tabuleiro.atualizar_posicao(3)
                    self.tabuleiro.pontos += 100
                    print("You move forward 3 spaces!")
                else:
                    print("You lost the fight!")
                    self.tabuleiro.atualizar_posicao(-3)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 3 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 021-> Poseidon
    def casa021(self):
        self.nome = "Poseidon"
        self.casa = 21
        self.texto = """Draw 1 card or move forward 2 spaces"""
        self.image = "image/casa_021.jpg"
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 2 spaces or [U] To use a card: ").upper().strip()
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must move 2 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(2)
                print(f"You moved 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 024 -> Ciclops
    def casa024(self):
        self.nome = "Ciclops"
        self.casa = 24
        self.image = "image/casa_024.jpg"
        self.texto = """If you are playing with Polyphemus, move forward 2 spaces.
Otherwise: engage in battle against the Cyclops and roll a die."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        if self.tabuleiro.nome_player == dic_players["1"]:  # Polifemo é a key "1" em dic_players
            self.tabuleiro.atualizar_posicao(2)
            print("Polyphemus does not need to fight his giant friends.\nMove forward 2 spaces.")
        else:
            while True:
                escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
                if escolha == "C":
                    if len(self.tabuleiro.cartas_player) == 0:
                        print("No cards available. You must roll the die.")
                        escolha = "D"
                    else:
                        self.tabuleiro.usar_carta()
                        break
                if escolha == "D":
                    resultado = randint(1, 6)
                    print(f"You rolled a {resultado}")
                    if resultado >= 4:
                        print("You won the fight!\nHurry up, Mount Olympus is still a long way off!")
                        self.tabuleiro.atualizar_posicao(1)
                        self.tabuleiro.points += 100
                        print("You move forward 1 space!")
                    else:
                        print("You lost the fight!")
                        self.tabuleiro.atualizar_posicao(-1)
                        self.tabuleiro.pontos -= 150
                        self.tabuleiro.vida -= 1
                        print("You move back 1 space and lose 1 life!")
                    break
                else:
                    print('Invalid choice! Please try again.')


    # 028 - > Harpias
    def casa028(self):
        self.nome = "Harpies"
        self.casa = 28
        self.image = "image/casa_028.jpg"
        self.texto = """Face the bronze-feathered monsters and roll 1 die.
If you win, move forward 1 space."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You won the fight!\nHurry up, Mount Olympus is still a long way off!")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 100
                    print("You move forward 1 space!")
                else:
                    print("You lost the fight!")
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 1 space and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # 030 - > Atena
    def casa030(self):
        self.nome = "Athena"
        self.casa = 30
        self.image = "image/casa_030.jpg"
        self.texto = """Receive Athena's blessings:
Draw a card, or move forward 1 space."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 1 space [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 1 space.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(1)
                print(f"You moved 1 space!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 32 - Tanatos # rever código , quando vai para caronte , caronte não funciona...
    def casa032(self):
        self.nome = "Thanatos"
        self.casa = 32
        self.image = "image/casa_032.jpg"
        self.texto = """Thanatos will take you to meet Charon. Advance to space 39."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [M] to meet Charon.").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. There's no turning back.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(7)
                print(f"You moved to space 39! There's no turning back.")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 34 - Minotauro
    def casa034(self):
        self.nome = "Minotaur"
        self.casa = 34
        self.image = "image/casa_034.jpg"
        self.texto = """Welcome to the Labyrinth of Crete.
Face the Minotaur! Fight the beast.
Roll 1 die, if you win, advance 2 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You won the Minotaur!\nHurry up, Mount Olympus is still a long way off!")
                    self.tabuleiro.atualizar_posicao(2)
                    self.tabuleiro.pontos += 100
                    print("You move forward 2 space!")
                else:
                    print("You lose the fight!")
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 1 space and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 36 - Labirinto
    def casa036(self):
        self.nome = "Labyrinth "
        self.casa = 36
        self.image = "image/casa_036.jpg"
        self.texto = """You are lost in the Labyrinth.
Seek Ariadne's thread, to escape you must roll the number 5 or 6."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 5:
                    print("You have successfully escaped the Labyrinth!")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 100
                    print("You move forward 1 space!")
                else:
                    print("You were unable to escape, go back 1 space!")
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 100
                    print("You move back 1 space!")
                break
            else:
                print('Invalid choice! Please try again.')


    # 038 - > Hades
    def casa038(self):
        self.nome = "Hades"
        self.casa = 38
        self.image = "image/casa_038.jpg"
        self.texto = """Avoid passing through Tartarus!
Draw a card or advance 2 spaces"""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 2 space [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 2 space.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(2)
                print(f"You moved 2 space!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 39 - Caronte
    def casa039(self):
        self.nome = "Charon"
        self.casa = 39
        self.texto = """Roll a die and negotiate your life with the ferryman of the River Styx."""
        self.image = "image/casa_039.jpg"
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have successfully crossed the River Styx."
                          "\nHurry up, Mount Olympus is still a long way off!")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 100
                    print("You move forward 1 space!")
                else:
                    print("You were unable to croos the River Styx, go back 2 space!")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 2 space and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 42 - Juízes
    def casa042(self):
        self.nome = "Judgment"
        self.casa = 42
        self.image = "image/casa_042.jpg"
        self.texto = """Be judged by the three judges:
Rhadamanthus, Minos and Aeacus.
Roll a die, and if you pass, advance to space 47."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have been judged worthy of leaving Hades.")
                    self.tabuleiro.atualizar_posicao(5)
                    self.tabuleiro.pontos += 100
                    print("You move forward to space 47!")
                else:
                    print("The judges have denied your request to leave Hades.\nMove back two spaces.")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 100
                    print("You move back 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 44 - Orfeu
    def casa044(self):
        self.nome = "Orpheus"
        self.casa = 44
        self.image = "image/casa_044.jpg"
        self.texto = """You are enchanted by Orpheus's sorrowful song.
Move back 1 space and lose 1 life."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [S] to stay here: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You will have to listen to Orpheus's song.")
                    escolha = "S"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "S":
                    print("You will have to listen to Orpheus's song.\nMove back 1 space and lose 1 life!")
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    break
            else:
                print('Invalid choice! Please try again.')


    # casa 49 - Hefesto
    def casa049(self):
        self.nome = "Hephaestus"
        self.casa = 49
        self.texto = """Draw a card or move forward 1 space."""
        self.image = "image/casa_049.jpg"
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 1 space [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 1 space.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(1)
                print(f"You moved 1 space!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 52 - Erinias
    def casa052(self):
        self.nome = "Erinyes"
        self.casa = 52
        self.image = "image/casa_052.jpg"
        self.texto = """Face the Furies and roll 1 die. If you win, move forward 2 spaces."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have been judged worthy to go on.")
                    self.tabuleiro.atualizar_posicao(2)
                    self.tabuleiro.pontos += 100
                    print("You move forward 2 spaces!")
                else:
                    print("The Erinyes have decided that you are not a good person!\n"
                          "Lose 1 life and move back 2 spaces.")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 2 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 55 - Deméter
    def casa055(self):
        self.nome = "Demeter"
        self.casa = 55
        self.image = "image/casa_055.jpg"
        self.texto = """Draw a card or move forward 1 space."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 1 space [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 1 space.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(1)
                print(f"You moved 1 space!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 61 - Hidra
    def casa061(self):
        self.nome = "Hydra"
        self.casa = 61
        self.image = "image/casa_061.jpg"
        self.texto = """Cutting off just one head won't be your salvation.
Roll a die. If you win, advance 2 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have emerged victorious from the battle!\nThe Hydra lies vanquished!")
                    self.tabuleiro.atualizar_posicao(2)
                    self.tabuleiro.pontos += 150
                    print("You move forward 2 spaces!")
                else:
                    print("You have fallen in battle! The Hydra still lives!")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 2 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 64 - Apolo
    def casa064(self):
        self.nome = "Apollo"
        self.casa = 64
        self.image = "image/casa_064.jpg"
        self.texto = """Draw a card or move forward 3 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 3 spaces [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 3 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(3)
                print(f"You moved 3 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 66 - Sisífo
    def casa066(self):
        self.nome = "Sisyphus"
        self.casa = 66
        self.texto = """Help the condemned king push his stone.
Lose one life, and return to space 57"""
        self.image = "image/casa_066.jpg"
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] To use a card or [S] To stay here.: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. Lose one life and return to to space 57.")
                    escolha = "S"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "S":
                self.tabuleiro.atualizar_posicao(-9)
                self.tabuleiro.vida -= 1
                self.tabuleiro.pontos -= 300
                print(f"You move back 9 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 069 -> Centauros
    def casa069(self):
        self.nome = "Centaurs"
        self.casa = 69
        self.texto = """The centaurs have drunk too much wine and have become violent.
If you are Hercules or Chiron, advance 3 spaces.
Otherwise, roll a die and try to defeat them."""
        self.image = "image/casa_069.jpg"
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        if self.tabuleiro.nome_player == dic_players["5"]:  # Chiron na key 5 do dic_players
            self.tabuleiro.atualizar_posicao(3)
            print("Chiron and Hercules don't need to fight the centaurs commanded by Dionysus.\nMove forward 3 spaces.")
        else:
            while True:
                escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
                if escolha == "C":
                    if len(self.tabuleiro.cartas_player) == 0:
                        print("No cards available. You must roll the die.")
                        escolha = "D"
                    else:
                        self.tabuleiro.usar_carta()
                        break
                if escolha == "D":
                    resultado = randint(1, 6)
                    print(f"You rolled a {resultado}")
                    if resultado >= 4:
                        print("You won the fight!\nHurry up, Mount Olympus is still a long way off!")
                        self.tabuleiro.atualizar_posicao(1)
                        self.tabuleiro.pontos += 100
                        print("You move forward 1 space!")
                    else:
                        print("You lost the fight!")
                        self.tabuleiro.atualizar_posicao(-1)
                        self.tabuleiro.pontos -= 150
                        self.tabuleiro.vida -= 1
                        print("You move back 1 space and lose 1 life!")
                    break
                else:
                    print('Invalid choice! Please try again.')


    # casa 71 -> Sátiros
    def casa071(self):
        self.nome = "Satyrs"
        self.casa = 71
        self.image = "image/casa_071.jpg"
        self.texto = """Some Satyrs from Dionysus' army are returning from their campaign in India.
And they won't let you pass.
Roll a die to try to defeat them.
If you give up on the battle, go back 3 spaces."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card, [M] to move back 3 spaces [D] To roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. Go back 3 spaces or fight against the Satyrs!")
                    escolha = input("Press [M] to move back 3 spaces or [D] to roll a die: ").upper().strip()
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(-3)
                print(f"You moved back 3 spaces!")
                break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You won the battle against the Satyrs!")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 100
                    print("You move forward 1 space!")
                else:
                    print("You were defeated by the Satyrs.\n"
                          "Lose 1 life and move back 2 spaces.")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 1 space and lose 1 life!\nNow you have to fight against the Centaurs!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 73 - Hera
    def casa073(self):
        self.nome = "Hera"
        self.casa = 73
        self.image = "image/casa_073.jpg"
        self.texto = """Draw a card or move forward 3 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 3 spaces [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 3 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(3)
                print(f"You moved 3 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 075 -> Sereias
    def casa075(self):
        self.nome = "Sirens"
        self.casa = 75
        self.image = "image/casa_075.jpg"
        self.texto = """Sirens! Roll a die to try to escape their terrible singing.
Medusa and Hippolyta are immune to their song and advance 2 spaces."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        # Hipolita na key 2 e Medusa na key 4 do dic_players
        if self.tabuleiro.nome_player == dic_players["2"] or  self.tabuleiro.nome_player == dic_players["4"]:
            self.tabuleiro.atualizar_posicao(3)
            print("Women are unaffected by the Sirens' song, Medusa or Hippolyta advance 2 spaces.")
        else:
            while True:
                escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
                if escolha == "C":
                    if len(self.tabuleiro.cartas_player) == 0:
                        print("No cards available. You must roll the die.")
                        escolha = "D"
                    else:
                        self.tabuleiro.usar_carta()
                        break
                if escolha == "D":
                    resultado = randint(1, 6)
                    print(f"You rolled a {resultado}")
                    if resultado >= 4:
                        print("You escaped the Sirens' song.\nHurry up, Mount Olympus is still a long way off!")
                        self.tabuleiro.atualizar_posicao(1)
                        self.tabuleiro.pontos += 100
                        print("You move forward 1 space!")
                    else:
                        print("You fell prey to the Sirens' song...")
                        self.tabuleiro.atualizar_posicao(-1)
                        self.tabuleiro.pontos -= 150
                        self.tabuleiro.vida -= 1
                        print("You move back 1 space and lose 1 life!")
                    break
                else:
                    print('Invalid choice! Please try again.')


    # casa 79 - Ares
    def casa079(self):
        self.nome = "Ares"
        self.casa = 79
        self.image = "image/casa_079.jpg"
        self.texto = """Face the god of war by rolling 1 die.
Ares can only be defeated if you roll a 6.
If you win, advance 10 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must fight and roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado == 6:
                    print("You have emerged victorious from the battle!\nAres was defeated!")
                    self.tabuleiro.atualizar_posicao(10)
                    self.tabuleiro.pontos += 300
                    print("You move forward 10 spaces!")
                else:
                    print("You have fallen in battle! Ares has won!")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("Move back 2 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 82 - Ninfas
    def casa082(self):
        self.nome = "Nymphs"
        self.casa = 82
        self.image = "image/casa_082.jpg"
        self.texto = """They have fallen in love with you and have decided to show you a shortcut.
Advance 2 spaces."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [N] to meet the Nymphs. ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must stay with the Nymphs.")
                    escolha = "N"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "N":
                self.tabuleiro.atualizar_posicao(2)
                self.tabuleiro.pontos += 100
                print("You move forward 2 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 85 - Tróia
    def casa085(self):
        self.nome = "Troy"
        self.casa = 85
        self.image = "image/casa_085.jpg"
        self.texto = """The great enemies of the Greeks will not let you pass without a fight.
In this battle, the Gods will not be able to help you, you cannot use cards,
roll 1 die, if you win, advance 2 spaces."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [D] to roll a die: ").upper().strip()
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have emerged victorious from the battle!\nThe Trojans have been defeated!")
                    self.tabuleiro.atualizar_posicao(2)
                    self.tabuleiro.pontos += 100
                    print("You move forward 2 spaces!")
                else:
                    print("You have fallen in battle! The Trojans has won!")
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("Move back 1 space and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 88 - Afrodite
    def casa088(self):
        self.nome = "Aphrodite"
        self.casa = 88
        self.image = "image/casa_088.jpg"
        self.texto = """Draw a card or move forward 3 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 3 spaces [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 3 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(3)
                print(f"You moved 3 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 90 - Eros
    def casa090(self):
        self.nome = "Eros"
        self.casa = 90
        self.image = "image/casa_090.jpg"
        self.texto = """You met Eros and were struck by love's arrow.
Return to the house of Aphrodite, the Goddess of beauty and Love."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [M] to meet the Goddess of beauty and Love. ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must to return to the house of Aphrodite.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(-2)
                print("You move back 2 spaces! Return to the house of Aphrodite")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 93 - Pegaso
    def casa093(self):
        self.nome = "Pegasus"
        self.casa = 93
        self.image = "image/casa_093.jpg"
        self.texto = """Hop on the winged horse and advance 6 spaces"""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [F] to fly with Pegasus. ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must to fly with Pegasus.")
                    escolha = "F"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "F":
                self.tabuleiro.atualizar_posicao(6)
                print("You move forward 6 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 96 - Dionisio
    def casa096(self):
        self.nome = "Dionisius"
        self.casa = 96
        self.image = "image/casa_096.jpg"
        self.texto = """Draw a card or move forward 3 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 3 spaces [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 3 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(3)
                print(f"You moved 3 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 98 - Bacantes
    def casa098(self):
        self.nome = "Bacchaes"
        self.casa = 98
        self.image = "image/casa_098.jpg"
        self.texto = """You fell into the Bacchae's orgy and drank too much wine during the party.
Move back 5 spaces and lose 1 life."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved back 5 spaces.")
                    self.tabuleiro.atualizar_posicao(-5)
                    self.tabuleiro.pontos -= 75
                else:
                    self.tabuleiro.usar_carta()
                    break
            else:
                print('Invalid choice! Please try again.')


    # casa 100 - Pan
    def casa100(self):
        self.nome = "Pan"
        self.casa = 100
        self.image = "image/casa_100.jpg"
        self.texto = """Upon hearing his chilling scream, you were so scared that you almost gave up on reaching Olympus.
Go back to space 94 and lost 1 life."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or go back to space 94 and lost 1 life").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved back 6 spaces and lose 1 life.")
                    self.tabuleiro.atualizar_posicao(-6)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                else:
                    self.tabuleiro.usar_carta()
                    break
            else:
                print('Invalid choice! Please try again.')


    # casa 104 - Artemis
    def casa104(self):
        self.nome = "Artemis"
        self.casa = 104
        self.image = "image/casa_104.jpg"
        self.texto = """Draw a card or move forward 4 spaces."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to gain a card, [M] to move 4 spaces [U] To use a card: ").upper().strip()
            if escolha == "C":
                self.tabuleiro.escolher_carta()
                break
            if escolha == "U":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You moved 4 spaces.")
                    escolha = "M"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "M":
                self.tabuleiro.atualizar_posicao(4)
                print(f"You moved 4 spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 107 - Órion
    def casa107(self):
        self.nome = "Orion"
        self.casa = 107
        self.image = "image/casa_107.jpg"
        self.texto = """The son of Poseidon was furious that you crossed his hunting grounds.
Roll 1 die and face the hunter."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You won the battle.")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 100
                    print("You move forward 1 space!")
                else:
                    print("You lose the battle!\n"
                          "Lose 1 life and move back 2 spaces.")
                    self.tabuleiro.atualizar_posicao(-2)
                    self.tabuleiro.pontos -= 150
                    self.tabuleiro.vida -= 1
                    print("You move back 2 spaces and lose 1 life!")
                break
            else:
                print('Invalid choice! Please try again.')

    # casa 110 - Midas
    def casa110(self):
            self.nome = "Midas"
            self.casa = 110
            self.image = "image/casa_110.jpg"
            self.texto = """The greedy king embraced you and you turned into a gold statue.
To reverse the transformation, return to Dionysus' house and seek the god's help."""
            print(f"This is the house of {self.nome}.")
            print(self.texto)
            while True:
                escolha = input("Press [C] to play a card or go back to Dionysus' house and lost 1 life").upper().strip()
                if escolha == "C":
                    if len(self.tabuleiro.cartas_player) == 0:
                        print("No cards available. You moved back 14 spaces and lose 1 life. ")
                        self.tabuleiro.atualizar_posicao(-14)
                        self.tabuleiro.pontos -= 150
                        self.tabuleiro.vida -= 1
                        break
                    else:
                        self.tabuleiro.usar_carta()
                        break
                else:
                    print('Invalid choice! Please try again.')


    # casa 112 - Zeus
    def casa112(self):
        self.nome = "Zeus"
        self.casa = 112
        self.image = "image/casa_112.jpg"
        self.texto = """Draw a card or roll 2 diece."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [C] to play a card or [D] to roll 2 diece: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the diece.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = (randint(1, 6)) + (randint(1, 6))
                print(f"You rolled a {resultado}")
                self.tabuleiro.atualizar_posicao(resultado)
                print(f"You move forward {resultado} spaces!")
                break
            else:
                print('Invalid choice! Please try again.')


    # casa 116 - Cronos
    def casa116(self):
        self.nome = "Chronos"
        self.casa = 116
        self.image = "image/casa_116.jpg"
        self.texto = """You have been trapped in time. Go back 5 spaces and lose 1 life."""
        print(f"This is the house of {self.nome}.")
        print(self.texto)
        while True:
                escolha = input(
                    "Press [C] to play a card or go back 5 spaces and lost 1 life").upper().strip()
                if escolha == "C":
                    if len(self.tabuleiro.cartas_player) == 0:
                        print("No cards available. You moved back 5 spaces and lose 1 life.")
                        self.tabuleiro.atualizar_posicao(-5)
                        self.tabuleiro.pontos -= 150
                        self.tabuleiro.vida -= 1
                    else:
                        self.tabuleiro.usar_carta()
                        break
                else:
                    print('Invalid choice! Please try again.')


    # casa 119 - Grifos
    def casa119(self):
        self.nome = "Griffins"
        self.casa = 119
        self.image = "image/casa_120.jpg"
        self.texto = """The entrance to Mount Olympus is heavily guarded.
You cannot use any God's help cards. Now, only your skill counts!
Roll 1 die to try to pass its guardians."""
        print(f"This is the house of the {self.nome}.")
        print(self.texto)
        while True:
            escolha = input("Press [D] to roll a die: ").upper().strip()
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    print("You have won!"
"Now you can ask the Gods for your boon!"
"They will grant it to you, or maybe not, who knows? "
"The Greek Gods are temperamental.")
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos += 1000
                    print("GAME OVER!")
                    print(f"Total points: {self.tabuleiro.pontos}")
                    break
                else:
                    print(f"The griffins didn't let you pass. Go back {resultado} spaces.")
                    self.tabuleiro.atualizar_posicao(-resultado)
                    self.tabuleiro.pontos -= 15 * resultado
                break
            else:
                print('Invalid choice! Please try again.')
        self.posicao_casas()

    # Funções genéricas - números aleatórios...

    # Se ganhar avança 1 casa, se perder volta 1 casa
    def retorna_avanca(self):
        print("""Watch out! You're under attack!
There are many other adventurers seeking to reach Mount Olympus
and receive the gifts of the Gods. They will do anything to defeat you.
Fight to continue and roll a die.
If you win, move forward 1 space.
If you lose, go back 1 space.""")
        while True:
            escolha = input("Press [C] to play a card or [D] to roll a die: ").upper().strip()
            if escolha == "C":
                if len(self.tabuleiro.cartas_player) == 0:
                    print("No cards available. You must roll the die.")
                    escolha = "D"
                else:
                    self.tabuleiro.usar_carta()
                    break
            if escolha == "D":
                resultado = randint(1, 6)
                print(f"You rolled a {resultado}")
                if resultado >= 4:
                    self.tabuleiro.atualizar_posicao(1)
                    self.tabuleiro.pontos -= 50
                    print("You move forward 1 space!")
                else:
                    self.tabuleiro.atualizar_posicao(-1)
                    self.tabuleiro.pontos -= 30
                    self.tabuleiro.vida -= 1
                    print("You move back 1 space.")
                break
            else:
                print('Invalid choice! Please try again.')





   # nova versão!!!
    def volta_casa(self): # não está removendo carta nehuma... rever código
        print("""The gods are unpredictable.
In this very moment, they have decided to hinder you.
Go back 1 space and lose 1 card.""")
        self.tabuleiro.atualizar_posicao(-1)
        self.tabuleiro.pontos -= 15

        if self.cartas_player:
            carta_removida = self.cartas_player.pop(self.cartas_player.index(choice(self.cartas_player)))
            print(f"You lost the card: {carta_removida.nome}")
        else:
            print("No cards to lose.")

        print("You move back 1 space.")


    """
    # Perde 1 carta e volta 1 casa 
    def volta_casa(self):
        print("The gods are unpredictable.
        In this very moment, they have decided to hinder you.
        Go back 1 space and lose 1 card.")
        self.tabuleiro.atualizar_posicao(-1)
        self.tabuleiro.pontos -= 15
        self.cartas_player.pop(self.cartas_player.index(carta_escolhida))# nova tentativa!
        #self.cartas_player.pop(0) # Crash aqui!! arrumar a instância!!!!
        print("You move back 1 space and lose 1 card.")
        self.posicao_casas()
    """

    # Avança 1 casa
    def avanca_casa(self):
        print("""Zephyrus decided to blow you a helping hand to get to Olympus faster.
The help of the gods is not always a good thing.
Move forward 1 space.""")
        self.tabuleiro.atualizar_posicao(1)
        print("You moved 1 space.")

















