class Animal():
    def __init__(self, esp, tam, hab, alm):
        self.especie = esp
        self.size = tam
        self.habt = hab
        self.alim = alm 

    def despl(self):
        print("El animal se esta dezplazando\n")

    def alimn(self):
        print("El animal se esta alimentando\n")

class Paloma(Animal):

    def __init__(self, esp, tam, hab, alm, sexo, color):
        super().__init__(esp, tam, hab, alm)
        self.sexo = sexo
        self.color = color

    def volar(self):
        print("La paloma ha alzado vuelo")

    def cnido(self):
        pass

paloma1 =Paloma("Ala Blanca","Pequeña","Ciudad","Omnivora","Hembra","Monocromatica")
print(paloma1.especie)

paloma1.despl()
paloma1.volar()
