from TDA.Dado import Dado
from TDA.Jugador import Jugador

class Juego7:
    def __init__(self, dado1, dado2, jugador):
        self.dado1 = dado1
        self.dado2 = dado2
        self.jugador = jugador

    def puedeJugar(self):
        return self.jugador.getCapital() >= self.jugador.getApuesta()

    def tirarDados(self):
        self.dado1.tirarDado()
        self.dado2.tirarDado()

    def getTotal(self):
        self.suma = int(self.dado1.getDado()+self.dado2.getDado())
        return self.suma
    
    def esGanador(self):
        monto = 0
        print("Juagada: "+str(self.jugador.jugada))
        if ((self.suma>7)&(int(self.jugador.getJugada())==1)):
            monto=self.jugador.getCapital()+self.jugador.getApuesta()
            self.jugador.setCapital(monto)
            return True
        elif ((self.suma<7)&(int(self.jugador.getJugada())==2)):
            monto=self.jugador.getCapital()+self.jugador.getApuesta()
            self.jugador.setCapital(monto)
            return True
        elif ((self.suma==7)&(int(self.jugador.getJugada())==3)):
            monto=self.jugador.getApuesta()*2+self.jugador.getCapital()
            self.jugador.setCapital(monto)
            return True
        else:
            monto=self.jugador.getCapital()-self.jugador.getApuesta()
            self.jugador.setCapital(monto)
            return False

    def getSuma(self):
        return self.suma

    def getDado1(self):
        return self.dado1
    
    def getDado2(self):
        return self.dado2