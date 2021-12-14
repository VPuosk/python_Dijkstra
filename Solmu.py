class Solmu:
    def __init__(self, indeksi, vertailuArvo):
        self.indeksi = indeksi
        self.vertailuArvo = vertailuArvo
        self.kaariLista = []
        self.vierailtu = False
        self.edeltävä = None

    def __repr__(self):
        return "(" + str(self.indeksi) + "-" + str(self.vertailuArvo) + ")" 
    
    def __str__(self):
        return "(" + str(self.indeksi) + "-" + str(self.vertailuArvo) + ")" 