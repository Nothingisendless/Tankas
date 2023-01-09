import random


class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.puse = "N"
        self.suviai = {'N': 0,'S': 0,'W': 0,'E': 0,}
        self.priesasx = random.randint(-10, 10)
        self.priesasy = random.randint(-10, 10)
        self.kuras = 10
        self.pataikymas = 0


    def pirmyn(self):
        self.y += 1
        self.puse = "N"
        self.kuras -= 1


    def atgal(self):
        self.y -= 1
        self.puse = "S"
        self.kuras -= 1


    def desinen(self):
        self.x += 1
        self.puse = "W"
        self.kuras -= 1


    def kairen(self):
        self.x -= 1
        self.puse = "E"
        self.kuras -= 1


    def sauti(self):
        self.suviai[self.puse] += 1
        if self.x == self.priesasx and self.puse == "N" and self.y <= self.priesasy:
            self.pataikymas += 1
            self.kuras += 5
        if self.x == self.priesasx and self.puse == "S" and self.y >= self.priesasy:
            self.pataikymas += 1
            self.kuras += 5
        if self.y == self.priesasy and self.puse == "E" and self.x <= self.priesasx:
            self.pataikymas += 1
            self.kuras += 5
        if self.y == self.priesasy and self.puse == "W" and self.x >= self.priesasx:
            self.pataikymas += 1
            self.kuras += 5

        print("Pataikei!")
        self.priesasx = random.randint(-10, 10)
        self.priesasy = random.randint(-10, 10)


    def pabaiga(self):
        if self.kuras == 0:
            print(f'Baigėsi kuras, žaidimo pabaiga')

            zaidejo_vardas = input("Įveskite savo vardą: ")
            zaideju_rezultatai = {}
            zaideju_rezultatai[zaidejo_vardas] = self.pataikymas
            


    def info(self):
        print(f'\nKoordinatės: X:{self.x}; Y:{self.y},'
              f'\nŽiūri į: {self.puse},'
              f'\nAtlikti šūviai į: {self.suviai},'
              f'\nViso atlikta šūvių: {sum(self.suviai.values())},'
              f'\nPriešo vieta:{self.priesasx, self.priesasy}'
              f'\nKuro kiekis bake:{self.kuras}'
              f'\nNukauta priešų:{self.pataikymas}')


tankas = Tankas()

while True:
    pasirinkimas = input("\nPasirinkite:\nw - į priekį \ns - atgal\na - į kairę\nd - į dešinę\nx - šauti\ni - info\n")
    if pasirinkimas == "w":
        tankas.pirmyn()
    if pasirinkimas == "s":
        tankas.atgal()
    if pasirinkimas == "a":
        tankas.kairen()
    if pasirinkimas == "d":
        tankas.desinen()
    if pasirinkimas == "x":
        tankas.sauti()
    if pasirinkimas == "i":
        tankas.info()
