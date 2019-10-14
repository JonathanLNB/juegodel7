from Juego7 import Juego7
from TDA.Dado import Dado
from TDA.Jugador import Jugador
import math


capital = 0
apuesta = math.inf

while(True):
    capital = float(input("Introduce Tu Capital: "))
    jugador = Jugador(capital)
    simulador = Juego7(Dado(), Dado(), jugador)
    while((apuesta>jugador.getCapital()) & (jugador.getCapital()>0.0)):
        apuesta = float(input("Introduce Tu Apuesta(Si Quiere Apostarlo Todo Introduce 0)\n\tTienes: ${}\n\t -> ".format(jugador.getCapital())))
        if(apuesta == 0):
            jugador.setApuesta(jugador.getCapital())
        else:
            if(apuesta <= jugador.getCapital()):
                jugador.setApuesta(apuesta)
            else:
                print("No tienes suficientes fondos :(")
        juego = int(input("Introduce La Jugada\n 1 Mayor a 7\n 2 Menor a 7\n 3 Igual a 7\n\t -> "))
        jugador.setJugada(juego)
        simulador.tirarDados()
        simulador.getTotal()
        if(simulador.esGanador()):
            print("\n\tGANASTE :3\nEl Valor del Primer Dado Fue De: {}\nEl Valor Del Segundo Dado Es Fue De: {}\nLa suma fue de {}\nTe quedan ${}".format(str(simulador.getDado1()), str(simulador.getDado2()), str(simulador.getSuma()), str(jugador.getCapital())))
        else:
            print("\n\tPERDISTE :(\nEl Valor del Primer Dado Fue De: {}\nEl Valor Del Segundo Dado Es Fue De: {}\nLa suma fue de {}\nTe quedan ${}".format(str(simulador.getDado1()), str(simulador.getDado2()), str(simulador.getSuma()), str(jugador.getCapital())))
        apuesta = math.inf
    op = int(input("¿Quieres volver a Jugar?\n 1) Si\n 2) No\n\t -> "))
    if(op!=1):
        break
print("¡Adios!")