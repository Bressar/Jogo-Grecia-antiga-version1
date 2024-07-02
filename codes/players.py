class Player:
    def __init__(self, name, about, image=None):
        self.__name = name
        self.__about = about
        self.__image = image


    def __str__(self):
        return f'{self.__name} \n{self.__about}'


polyphemus = Player("Polyphemus", """
Cyclopean giant Poliphemus, son of Poseidon,
guards his flock with a single eye.
He wants to reach Olympus to seek revenge on Odysseus.""", "imagem_base/polifemo.jpg")

hippolyta = Player("Hippolyta", """
Hippolyta, queen of the Amazons: A powerful warrior
and ruler of a legendary race of female warriors.
She wants to reach Olympus to attain the status of a demigoddess.""")

odysseus = Player("Odysseus", """
Odysseus, king of Ithaca, outsmarts monsters and gods
on his epic journey home after the Trojan War.
He wants to reach Olympus to attain the status of a demigod.""")

medusa = Player("Medusa", """
Once a beautiful maiden, cursed by a jealous god,
Medusa's gaze turns men to stone.
She seeks to reach Olympus to regain her human form.""")

chiron = Player("Chiron", """
Wise centaur Chiron, famed for his knowledge and healing skills,
tutored many heroes like Achilles, instilling in them courage and virtue.
He want to reach Olympus to be cured of an 'incurable' poison.""")

dic_players = {
    "1": polyphemus,
    "2": hippolyta,
    "3": odysseus,
    "4": medusa,
    "5": chiron
}

