# yksinkertainen lukija, joka tulkitsee saamansa tiedoston
# ja pyydettäessä palauttaa sen taulukoituna tietona

class Filereader:
    def __init__(self, nimi):
        try:
            self.file = open(nimi, "rt")
        except OSError:
            self.file = None
            print("Tiedostoa {0} ei voitu avata".format(nimi))

    def PalautaRivit(self):
        rivit = []
        for rivi in self.file:
            sisältö = rivi.rstrip('\r\n').split(' ')
            rivit.append(sisältö)
        return rivit

    def Sulje(self):
        self.file.close()