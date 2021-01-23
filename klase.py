class Prikaz(object):
    def pokaziPocetakIgre(self):
        print("*"*50)
        print("*"*20+" CONNECT4 "+"*"*20)
        print("*"*50)
    def unesiIgraca(self):
        while True:
            igrac1 = input("Odaberite boju žetona 'C' ili 'P' ")
            if igrac1.upper() == 'C':
                igrac2='P'
                print("Odabrali ste " + igrac1 + ". Igrac2 će imati boju: " + igrac2)
                return igrac1.upper(),igrac2
            elif igrac1.upper() == 'P':
                igrac2='C'
                print("Odabrali ste " + igrac1 + ". Igrac2 će imati boju: " + igrac2)
                return igrac1.upper(),igrac2
            else:
                print("Molimo vas odaberite 'P' ili 'C' ")
      
class Bodovanje():
    def __init__(self):
        self.brojStupaca = 7
        self.brojRedova = 6
        self.ploca = [ [ '  ' for i in range( self.brojStupaca)] for i in range(self.brojRedova) ]
    def prikaziPlocu(self):
        for i, linija in enumerate(self.ploca):
            print("_" * self.brojStupaca * 4)
            print(*linija, sep=' |')
        print('   '.join(str(x) for x in range(self.brojStupaca)))
    def odabirPolja(self):
        polje=17
        while polje>6:
            polje = int(input("Molimo vas odaberite polje između 0 i 6 : "))
                  
        while self.ploca[0][polje] != '  ':
            polje = int(input("Ovo polje je puno. Molimo vas odaberite polje između 0 i 6 :  "))
        #if ploca[0][0]!= '  ' and ploca[0][1]!= '  ' and ploca[0][2]!= '  ' and ploca[0][3]!= '  ' and ploca[0][4]!= '  ' and ploca[0][5]!= '  ' and ploca[0][6]!= '  ':
         #   print("Igra gotova. Neriješeno!")
        return polje  
        
    def jeSlobodnoPolje(self, linija, stupac):
        if linija[stupac] == '  ':
            return True
        return False

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
    
    def igraj(self, stupacIgraca, marker):
        for item in reversed(self.ploca):
            if self.jeSlobodnoPolje(item, stupacIgraca):
                item[stupacIgraca] = " " + marker
                return True
        return False
    
class Igraci():
    ime1=""
    ime2=""
    while True:
        ime1 = input("Unesite ime prvog igrača: ")
        if len(ime1)>=1:
            print("Igrač 1 : "+ime1)
            break
    while True:
        ime2 = input("Unesite ime drugog igrača: ")
        if len(ime2)>=1:
            print("Igrač 2 : "+ime2)
            break           
               
p=Prikaz()
b=Bodovanje()
i=Igraci()

class Igra(object):
    pocetak=True
    while pocetak:
        #pokaži naslov
        p.pokaziPocetakIgre()
        #igrač odabire boju žetona
        igraci=p.unesiIgraca()
        #pokaži ploču
        b.prikaziPlocu()
        pobjeda=False
        y=1
        while not pobjeda:
            #počinjemo igrati
            if y%2==0:
                trenutniIgrac=i.ime2
                marker=igraci[1]
            else:
                trenutniIgrac=i.ime1
                marker=igraci[0]
            #igrač bira polje
            pozicija=b.odabirPolja()
            if not b.igraj(pozicija, marker):
                print(f"Stupac {pozicija} popunjen")
            #generiramo obrnutu ploču
            obrnutaPloca=b.napraviObrnutuPlocu()
            #Provjerimo je li pobjeda
            if b.provjeriLiniju(marker) or b.provjeriLiniju(marker, obrnutaPloca) or b.provjeriDiagonalu(marker):
                #mjenjamo pobjedu u True i izazimo iz petlje
                pobjeda=True
                b.prikaziPlocu()
                print(f"Pobjedio je {trenutniIgrac}")
                #nudimo mogučnost ponovne igre DA/NE
                #Ako DA, resetiramo klasu s novim podacima
                replay=input("Želite li ponovo igrati (DA/NE) ?")
                if replay.lower()=="ne":
                    pocetak=False
                    print("Igra gotova")
                else:
                    p=Prikaz()
                    b=Bodovanje()
                break
            b.prikaziPlocu()
            y+=1
                

        
