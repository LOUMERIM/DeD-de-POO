import random
from abc import ABC, abstractmethod

class Person(ABC): #Atributos iniciais dos personagens
    def __init__(self, name):
        self.name=name
        self.energy=100
        self.sorte=random.randint(1, 12)
        self.historico_batalhas=[]

    def cura(self, quantidade): #Atributo da cura
        self.energy=min(self.energy+quantidade,10)

    def morte(self, quantidade): #Atributo da morte
        self.energy=max(self.energy-quantidade,0)
        if self.energy==0:
            print(f"{self.name} está morto!")

    @abstractmethod
    def sorteio(self):
        pass

    @abstractmethod
    def interagir(self, outro_person):
        pass


class Heroi(Person): #Classe do Mocinho
    def sorteio(self):
        return random.randint(1, 12)

    def interagir(self, outro_person):
        if self.energy>0: #Caso esteja vivo, dá de interagir
            print(f"{self.name} está conversando com {outro_person.name}.")
            outro_person.cura(1)
        else:
            print(f"{self.name} está morto e não pode interagir.")

    def lutar(self, oponente): #Atributo da luta
        if self.energy>0 and oponente.energy>0:
            resultado_mocinho=self.sorteio()
            resultado_oponente=oponente.sorteio()
            if resultado_mocinho>resultado_oponente:
                self.cura(2)
                oponente.morte(2)
                self.historico_batalhas.append(f"Vitória contra {oponente.name}")
                oponente.historico_batalhas.append(f"Derrota para {self.name}")
            elif resultado_mocinho<resultado_oponente:
                self.morte(2)
                oponente.cura(2)
                self.historico_batalhas.append(f"Derrota para {oponente.name}")
                oponente.historico_batalhas.append(f"Vitória contra {self.name}")
            else:
                self.morte(1)
                oponente.morte(1)
                self.historico_batalhas.append(f"Empate com {oponente.name}")
                oponente.historico_batalhas.append(f"Empate com {self.name}")
        else:
            print("Um dos personagens está morto e não pode lutar.")


class Vilao(Person): #Classe do Vilao
    def sorteio(self):
        return random.randint(1, 12)

    def interagir(self, outro_person):
        if self.energy>0: #Interação igual do Heroi, porem claro, depreciativamente
            print(f"{self.name} está esnobando de {outro_person.name}.")
            outro_person.morte(1)
        else:
            print(f"{self.name} está morto e não pode interagir.")

    def lutar(self, oponente): #Atributo da luta também
        if self.energy>0 and oponente.energy>0:
            resultado_vilao=self.sorteio()
            resultado_oponente=oponente.sorteio()
            if resultado_vilao>resultado_oponente:
                self.cura(2)
                oponente.morte(2)
                self.historico_batalhas.append(f"Vitória contra {oponente.name}")
                oponente.historico_batalhas.append(f"Derrota para {self.name}")
            elif resultado_vilao<resultado_oponente:
                self.morte(2)
                oponente.cura(2)
                self.historico_batalhas.append(f"Derrota para {oponente.name}")
                oponente.historico_batalhas.append(f"Vitória contra {self.name}")
            else:
                self.morte(1)
                oponente.morte(1)
                self.historico_batalhas.append(f"Empate com {oponente.name}")
                oponente.historico_batalhas.append(f"Empate com {self.name}")
        else:
            print("Um dos personagens está morto e não pode lutar.")
