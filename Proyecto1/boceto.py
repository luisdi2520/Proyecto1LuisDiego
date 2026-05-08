import tkinter as tk 
from logica import load_Personajes, Crearhollows
from pantalla import PantallaInicio
from mapa import Mapa
from batalla import Batalla
pantalla_act = None
equip = None
equipHollow = None
puntajeTotal = 0
def iniciar(nombre, equipo, avatar):
     global pantalla_act, equip, equipHollow, nombreJuga,avatarJuga
     equip = equipo
     nombreJuga = nombre
     avatarJuga = avatar
     pantalla_act.destroy()
     equipHollow = Crearhollows(personajes)
     mapa = Mapa(ventana, equipHollow, iniBatalla=ab_batalla)
     mapa.pack(fill="both", expand=True)
     pantalla_act = mapa

def ab_batalla(hollow):
    global pantalla_act
    pantalla_act.destroy()
    ventana.update()
    batalla = Batalla(ventana, nombreJuga, equip, hollow, avatarJuga, fin= volverMapa)
    batalla.pack(fill="both", expand=True)
    pantalla_act = batalla

def volverMapa(puntaje):
     global pantalla_act, puntajeTotal
     puntajeTotal += puntaje
     pantalla_act.destroy()
     ventana.update()
     mapa = Mapa(ventana, equipHollow, iniBatalla=ab_batalla)
     mapa.pack(fill="both", expand=True)
     pantalla_act = mapa
personajes = load_Personajes()

ventana = tk.Tk() 
ventana.title("Disney's Epic Adventure")
ventana. geometry("400x600")

pantalla_act= PantallaInicio(ventana, personajes, inicio= iniciar)
pantalla_act.pack(fill="both", expand =True)

ventana.mainloop()
