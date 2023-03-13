class Telewizor:
    def __init__(self, kanal=1, glosnosc=10 ):
        self.kanal = kanal
        self.glosnosc = glosnosc

    @property
    def kanal(self):
        return self._kanal

    @kanal.setter
    def kanal(self, value):
        if value < 1:
            self._kanal = 1
        elif value > 100:
            self._kanal = 100
        else:
            self._kanal = value

    @property
    def glosnosc(self):
        return self._glosnosc

    @glosnosc.setter
    def glosnosc(self, value):
        if value < 0:
            self._glosnosc = 0
        elif value > 20:
            self._glosnosc = 20
        else:
            self._glosnosc = value

    def zmien_kanal(self, numer):
        self.kanal = numer

    def zwieksz_glosnosc(self):
        self.glosnosc += 1

    def zmniejsz_glosnosc(self):
        self.glosnosc -= 1

tv = Telewizor()
while True:
    print("Aktualny kanał:", tv.kanal)
    print("Aktualna glosnosc:", tv.glosnosc)
    print("1 - Zmien kanal")
    print("2 - Zwieksz glosnosc")
    print("3 - Zmniejsz glosnosc")
    print("0 - Wyjdz")
    wybor = int(input("Wybierz opcję:"))

    if wybor == 0:
        break
    elif wybor == 1:
        numer = int(input("Podaj numer kanalu:"))
        tv.zmien_kanal(numer)
    elif wybor == 2:
        tv.zwieksz_glosnosc()
    elif wybor == 3:
        tv.zmniejsz_glosnosc()
    else:
        print("Nieprawidlowa opcja!")
