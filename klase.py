class Prikaz:
    def __init__(self):
        self.brojStupaca = 7
        self.brojRedova = 6
        self.ploca = [ [ '  ' for i in range( self.brojStupaca)] for i in range(self.brojRedova) ]
    def displayPloca(self):
        for i, linija in enumerate(self.ploca):
            
            print("_" * self.brojStupaca * 4)

            print(*linija, sep=' |')

        print('    '.join(str(x) for x in range(self.brojStupaca)))
    def jeSlobodnoPolje(self, linija, stupac):
        if linija[stupac] == '  ':
            return True
        return False
    
class Igrac:
    def igrac_zeton(self):
        igrac1 = input("Odaberite boju žetona 'C' ili 'P' ")
        while True:
            if igrac1.upper() == 'C':
                igrac2='P'
                print("Odabrali ste " + igrac1 + ". Igrac2 će imati boju: " + igrac2)
                return igrac1.upper(),igrac2
            elif igrac1.upper() == 'P':
                igrac2='C'
                print("Odabrali ste " + igrac1 + ". Igrac2 će imati boju: " + igrac2)
                return igrac1.upper(),igrac2
            else:
                igrac1 = input("Molimo vas odaberite 'P' ili 'C' ")
class Igra:
    def odabir_polja(self):
        polje = int(input("Molimo vas odaberite polje između 0 i 6 : "))
        while self.ploca[0][polje] != '  ':
            polje = int(input("Ovo polje je puno. Molimo vas odaberite polje između 0 i 6 :  "))
        return polje
        def provjeriLiniju(self, marker, ploca=None):
            if ploca is None:
                ploca=self.ploca
        # Provjeri liniju
            for linija in ploca:
                for i in range(0,len(linija)):
                    if i < len(linija) - 3:
                        if linija[i] == linija[i+1] == linija[i+2] == linija[i+3] == " " + marker:
                            return True

    def provjeriDiagonalu(self, marker):
        diagPloca = []
        for i, linija in enumerate(self.ploca):
            for index, item in enumerate(linija):
                if item == ' ' + marker:
                    diagPloca.append(int(str(i)+str(index)))

        for item in diagPloca:
            if int(item) + 11 in diagPloca and int(item) + 22 in diagPloca and int(item) + 33 in diagPloca:
                return True
        #obrnuta
        for item in reversed(diagPloca):
            if int(item) - 9 in diagPloca and int(item) - 18 in diagPloca and int(item) - 27 in diagPloca:
                return True

    def napraviObrnutuPlocu(self):
        obrnutaPloca = []
        for linija in self.ploca:
            for index, item in enumerate(linija):
                try:
                    obrnutaPloca[index].append(item)
                except:
                    obrnutaPloca.append([])
                    obrnutaPloca[index].append(item)
        return obrnutaPloca

    def igra(self, stupacIgraca, marker):
        for item in reversed(self.ploca):
            if self.jeSlobodnoPolje(item, stupacIgraca):
                item[stupacIgraca] = " " + marker
                return True
        return False
c=Prikaz()
