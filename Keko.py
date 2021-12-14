from Solmu import *

# sorttaava KekoOlio, rakennettu niin että 'olio' voi olla
# mitä tahansa
class KekoOlio:
    def __init__(self, olio, vertailu):
        self.olio = olio
        self.arvo = vertailu

# Varsinainen keko (minimikeko)
class Keko:
    def __repr__(self):
        return "Keko()"

    def __str__(self):
        return str(self.kekoLista) + " - " + str(self.keonKoko)

    def __init__(self):
        self.kekoLista = [ 0 ]
        self.keonKoko = 0

    # Palauttaa seon ensimmäisen arvon
    # poistaa ko. arvon keosta ja aloittaa
    # keon uudelleen järjestämisen.
    def otaEnsimmäinen(self):
        if (self.keonKoko == 0):
            return None
        palautus = self.kekoLista[1]
        self.vaihda(1, self.keonKoko)
        self.keonKoko -= 1
        self.jarjestaAlas(1)
        return palautus

    # Vaihtaa päittäin keossa olevat KekoOliot
    def vaihda(self, ensimmäinenIndeksi, toinenIndeksi):
        temp = self.kekoLista[ensimmäinenIndeksi]
        self.kekoLista[ensimmäinenIndeksi] = self.kekoLista[toinenIndeksi]
        self.kekoLista[toinenIndeksi] = temp

    # Järjestää keon alhaalta ylöspäin
    # Eli suurista indeksiarvoista pieniin
    # pieniin indeksiarvoihin
    def jarjestaYlos(self, indeksi):
        uusiIndeksi = int(indeksi / 2)

        if uusiIndeksi < 1:
            return
        
        if (self.kekoLista[indeksi].arvo < self.kekoLista[uusiIndeksi].arvo):
            self.vaihda(indeksi, uusiIndeksi)
            self.jarjestaYlos(uusiIndeksi)

    # Lisää kekoon uuden kekoolion, tarvittaessa
    # luo uuden olin ja pidentää keon rungon
    # muodostavaa taulukkoa. Aloittaa keon
    # uudelleen järjestyksen
    def lisääUusi(self, olio, vertailu):
        self.keonKoko += 1
        uusiOlio = KekoOlio(olio, vertailu)

        # tarvitsee lisätä uusi
        if (len(self.kekoLista) <= self.keonKoko):
            self.kekoLista.append(uusiOlio)
            self.jarjestaYlos(self.keonKoko)
        # ei tarvitse lisätä uutta
        else:
            self.kekoLista[self.keonKoko] = uusiOlio
            self.jarjestaYlos(self.keonKoko)       

    # Järjestää keokoa pienestä indeksiarvosta suuria
    # indeksiarvoja kohden
    def jarjestaAlas(self, indeksi):
        alempiIndeksi = indeksi * 2
        ylempiIndeksi = alempiIndeksi + 1

        if self.keonKoko < alempiIndeksi:
            return
        
        if self.keonKoko == alempiIndeksi:
            if (self.kekoLista[indeksi].arvo > self.kekoLista[alempiIndeksi].arvo):
                self.vaihda(indeksi, alempiIndeksi)
                self.jarjestaAlas(alempiIndeksi)
            return
        
        if (self.kekoLista[ylempiIndeksi].arvo < self.kekoLista[alempiIndeksi].arvo):
            alempiIndeksi = ylempiIndeksi
        
        if (self.kekoLista[indeksi].arvo > self.kekoLista[alempiIndeksi].arvo):
            self.vaihda(indeksi, alempiIndeksi)
            self.jarjestaAlas(alempiIndeksi)