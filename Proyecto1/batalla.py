import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox
from logica import turnos, elecc_pjHollow

class Batalla(tk.Frame):
    def __init__(self, master, jugador, equip, hollow, avatar, fin):
        super().__init__(master)
        self.master = master
        self.jugador = jugador
        self.equip = equip
        self.hollow = hollow
        self.avatar = avatar
        self.fin = fin 

        self.p_jugador = None
        self.p_hollow = None 
        self.turno = 0
        self.puntajeJugador = 0
        self.puntajeHollow = 0

        self.pantalla()
        self.cargarAva()
        self.elegirPJ_ini()
    
    def pantalla(self):
        label = tk.Label(self, text="BATALLA", font=("Arial", 20, "bold"))
        label.pack(pady=10)
        juga = tk.Label(self, text=f"Jugador: {self.jugador}")
        juga.pack()
        self.imgAva = tk.Label(self)
        self.imgAva.pack()
        self.label_hollow = tk.Label(self, text="")
        self.label_hollow.pack()
        self.hp_hollow = tk.Label(self, text="")
        self.hp_hollow.pack()
        self.img_hollow = tk.Label(self)
        self.img_hollow.pack()

        self.label_jugador = tk.Label(self, text="")
        self.label_jugador.pack()
        self.hp_jugador = tk.Label(self, text="")
        self.hp_jugador.pack()
        self.img_jugador = tk.Label(self)
        self.img_jugador.pack()

        self.logText = tk.Text(self, height=8, state="disabled")
        self.logText.pack()

        self.labelPuntaje = tk.Label(self, text="Puntaje - Jugador: 0 | Hollow: 0")
        self.labelPuntaje.pack()

        atacar = tk.Button(self,text="ATACAR", command=self.atacar)
        atacar.pack(pady=5)
        PJ = tk.Button(self,text="EQUIPO", command=self.cambiarPJ)
        PJ.pack()
    
    def cargarAva(self):
        imgAva = Image.open(f"Imagenes/avatares/{self.avatar}")
        imgAva = imgAva.resize((80,80))
        foto = ImageTk.PhotoImage(imgAva)
        self.imgAva.config(image=foto)
        self.imgAva.image = foto


    def elegirPJ_ini(self):
        #Hollow
        self.p_hollow = elecc_pjHollow(self.hollow)
        self.actualizarPantalla()

        #Jugador
        self.cambiarPJ()

    def atacar(self):
        if self.p_jugador is None or self.p_hollow is None:
            return 
        log = []
        turnos(self.turno, self.p_jugador, self.p_hollow, log)
        self.mostrarLog(log)
        self.actualizarPantalla()
        self.veriKO()        

        self.turno +=2
    
    def cambiarPJ(self):
        dispo =[p for p in self.equip if not p["KO"]]
        if not dispo:
            return 
        win_cambio = tk.Toplevel(self.master)
        win_cambio.title("Elige personaje")
        for p in dispo:
         boton = tk.Button(win_cambio, text=f"{p['nombre']}(HP:{p['hp']})",command=lambda per=p, w=win_cambio: self.selecc(per, w))
         boton.pack(pady=3)

    def selecc(self, personaje, ventana):
        self.p_jugador = personaje
        ventana.destroy()
        self.actualizarPantalla()
    
    def actualizarPantalla(self):
        if self.p_hollow:
            self.label_hollow.config(text=f"{self.p_hollow['nombre']}")
            self.hp_hollow.config(text=f"HP:{self.p_hollow['hp']}")
            ima = Image.open(f"Imagenes/{self.p_hollow['imagen']}")
            ima = ima.resize((100,100))
            foto = ImageTk.PhotoImage(ima)
            self.img_hollow.config(image=foto)
            self.img_hollow.image = foto 
        if self.p_jugador:
            self.label_jugador.config(text=f"{self.p_jugador['nombre']}")
            self.hp_jugador.config(text=f"HP:{self.p_jugador['hp']}")
            imaJuga = Image.open(f"Imagenes/{self.p_jugador['imagen']}")
            imaJuga = imaJuga.resize((100,100))
            foto = ImageTk.PhotoImage(imaJuga)
            self.img_jugador.config(image=foto)
            self.img_jugador.image = foto
        self.labelPuntaje.config(text=f"Puntaje - Jugador: {self.puntajeJugador} | Hollow: {self.puntajeHollow}")
    
    def mostrarLog(self, log):
        self.logText.config(state="normal")
        for mensaje in log:
            self.logText.insert(tk.END, mensaje + "\n")
        self.logText.config(state="disabled")
    
    def veriKO(self):
        if self.p_hollow and self.p_hollow["KO"]:
            self.p_hollow["hp"] = self.p_hollow["max_hp"]  
            self.p_hollow["KO"] = False
            self.equip.append(self.p_hollow)
            self.puntajeJugador += 1
            self.hollow["personajes"].remove(self.p_hollow)
            self.p_hollow = elecc_pjHollow(self.hollow)
        if self.p_jugador and self.p_jugador["KO"]:
             self.p_jugador["hp"] = self.p_jugador["max_hp"]  
             self.p_jugador["KO"] = False
             self.hollow["personajes"].append(self.p_jugador)
             self.puntajeHollow += 1
             self.equip.remove(self.p_jugador)
             self.p_jugador = None
        self.actualizarPantalla()
        self.verificarFin()
    
    def verificarFin(self):
        dispo_jugador = [p for p in self.equip if not p["KO"]]
        dispo_hollow = [p for p in self.hollow["personajes"] if not p["KO"]]

        if not dispo_hollow:
            self.hollow["vencido"] = True
            messagebox.showinfo("Ganaste", f"Venciste al {self.hollow['nombre']}")
            self.fin(self.puntajeJugador)
        elif not dispo_jugador:
            messagebox.showinfo("Perdiste", f"El{self.hollow['nombre']} te vencio")
            self.fin(self.puntajeJugador)