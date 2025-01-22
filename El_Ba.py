# ----------------------------------------------------------------------------------
import random
class El_Ba:
    def __init__(self, jaa, ba, gestiones_del_ba, frases):
        self.jaa = jaa
        self.ba = ba
        self.gestiones = gestiones_del_ba
        self.frases = frases
    def hacer_examenes(self):
        print("Creo que apruebo discreta...", "He sacado un 1.44")
    def politono(self):
        print(f" Bieeen {self.jaa}, tenia nuevo politono ero me lo borro mi mdre")
        print("Era mi madre diciendo un bote de mierda")
        print("El bote de la ruleta?")
    def mostrar_gestiones(self):
        for GRAN_GESTION in enumerate(self.gestiones):
            print(GRAN_GESTION, "del ", self.ba)
    def hacer_llorar(self):
        frase = random.choice(self.frases)
        return frase
    def adios():
        return "Yo desconecto"

Padre_ElBa = El_Ba("jaa", "Ba", ["Chupada en infi", "Jaa", "El Álex Ba.. Esta jugoso"], 
["Es igual, no entra en infi", "Mejor en chino", "Se puede rezar al corán"])

Padre_ElBa.hacer_examenes()
Padre_ElBa.politono()
print("Tipica frase del Ba: ", Padre_ElBa.hacer_llorar())
print(Padre_ElBa.adios())



















