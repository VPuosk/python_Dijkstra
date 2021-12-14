from Keko import *
from Filereader import *
from Kaari import *
from Solmu import *
import sys

# Tekee dijkstran algoritmin mukaisen reitinhaun
# Syötettävän tiedon tulee olla ASCII muotoista
# 1. rivin tulee sisältää seuraavat tiedot:
#       alkusolmu loppusolmu
# kaikki muut rivit sisältävät kaaritietoa, joka
# tulee olla muodossa:
#       kaarenalku kaarenloppu paino
# painon tulee olla positiivinen (nollaa suurempi)
# kokonaisluku.

def main(args):
    kokonaan = False

    if "kokonaan" in args:
        kokonaan = True
    
    # määritetään käsiteltävä tiedosto (voisi antaa argumenttinakin)
    tiedosto = "testi.txt"
    avattuTiedosto = Filereader(tiedosto)

    if avattuTiedosto == None:
        return
    
    tiedot = avattuTiedosto.PalautaRivit()

    avattuTiedosto.Sulje()

    # tarkistetaan syötettä
    # mikäli ei ole tietoja, lopeta
    if len(tiedot) == 0:
        print("Virhe, ei syötettä")
        return

    # mikäli tiedot ovat ongelmallisia, lopeta
    if len(tiedot[0]) != 2:
        print("Virhe kentässä: {0}".format(str(tiedot[0])))
        return

    # alustetaan tietorakenteita
    solmut = {}
    dKeko = Keko()
    
    # luetaan alku ja loppusolmun tiedot
    alku = tiedot[0][0]
    loppu = tiedot[0][1]

    # luodaan alku ja loppusolmu
    solmut[alku] = Solmu(alku, -1)
    solmut[loppu] = Solmu(loppu, -1)

    # käydään läpi muut syötetyt tiedot
    for idx in range(1, len(tiedot)):
        tietokenttä = tiedot[idx]

        # mikäli tiedot ovat ongelmallisia, lopeta
        if len(tietokenttä) != 3:
            print("Virhe kentässä: {0}".format(str(tietokenttä)))
            return

        kaarenAlkuSolmunNimi = tietokenttä[0]
        kaarenLoppuSolmunNimi = tietokenttä[1]
        kaarenPaino = int(tietokenttä[2])

        # varmistetaan, että solmut ovat olemassa, jos eivät ole
        # niin silloin ne luodaan tässä vaiheessa
        if not kaarenAlkuSolmunNimi in solmut:
            solmut[kaarenAlkuSolmunNimi] = Solmu(kaarenAlkuSolmunNimi, -1)

        if not kaarenLoppuSolmunNimi in solmut:
            solmut[kaarenLoppuSolmunNimi] = Solmu(kaarenLoppuSolmunNimi, -1)
        
        # luodaan kaaret, lisätään myös vastakaaret
        uusiKaari = Kaari(tietokenttä[0], tietokenttä[1], int(tietokenttä[2]))
        vastaKaari = Kaari(tietokenttä[1], tietokenttä[0], int(tietokenttä[2]))
        uusiKaari.vasta = vastaKaari
        vastaKaari.vasta = uusiKaari

        # lisätään kaaret kunkin solmun kaarilistaan
        solmut[kaarenAlkuSolmunNimi].kaariLista.append(uusiKaari)
        solmut[kaarenLoppuSolmunNimi].kaariLista.append(vastaKaari)

    # lisätään aloitussolmu kekoon
    solmut[alku].vertailuArvo = 0
    dKeko.lisääUusi(solmut[alku],0)

    # varsinainen hakulooppi
    while dKeko.keonKoko > 0:
        solmu = dKeko.otaEnsimmäinen().olio

        # katsotaan onko täällä jo käyty
        # jos ei ole, niin nyt on
        if (solmu.vierailtu):
            continue
        else:
            solmu.vierailtu = True

        # print(solmu)

        # katsotaan onko tämä loppusolmu
        if ((solmu.indeksi == loppu) and (not kokonaan)):
            # homma tuli valmiiksi
            break

        # katsotaan mihin tästä pääsee
        for kaari in solmu.kaariLista:
            uusiSolmu = solmut[kaari.loppu]

            # täällä on jo käyty
            if (uusiSolmu.vierailtu):
                continue
            
            # aletaan vertailla etäisyyksiä
            nykVertailuArvo = uusiSolmu.vertailuArvo
            uusiVertailuArvo = solmu.vertailuArvo + kaari.paino

            # solmua ei oltu vielä kertaakaan lisätty, tehdään se nyt
            # TAI jos ehto ei täyty, niin keossa on jo paremmalla
            # vertailuarvolla oleva solmu
            if ((nykVertailuArvo == -1) or (nykVertailuArvo > uusiVertailuArvo)):
                uusiSolmu.vertailuArvo = uusiVertailuArvo
                uusiSolmu.edeltävä = solmu
                dKeko.lisääUusi(uusiSolmu, uusiVertailuArvo)

    # tulostuksia
    # ensin varsinainen tulosrivi:
    print("\nLyhin reitti solmusta {1} solmuun {2}: {0}\n".format(solmut[loppu].vertailuArvo, alku, loppu))

    # sitten solmu kohtainen tuloskatsaus
    # HUOM! haku päättyy kun 'maalisolmu'
    # saavutetaan.
    print("Kaikki solmut ja niiden tulokset:")
    for x in solmut.items():
        print("\t{0} - arvo: {1}".format(x, x[1].vertailuArvo))
    
main(sys.argv[1:])
