import tkinter as tk

class Mapa(tk.Frame):
    def __init__(self, master, hollows, iniBatalla):
        super().__init__(master)
        self.master = master
        self.hollows = hollows
        self.iniBatalla = iniBatalla
        self.pantalla()
    
    def pantalla(self):
        label = tk.Label(self, text="Mapa del Reino", font=("Arial", 20, "bold"))
        label.pack(pady=10)
        selecHollow = tk.Label(self, text="Selecciona un hollow", font=("Arial", 20, "bold"))
        selecHollow.pack()

        for i, hollow in  enumerate (self.hollows):
            if hollow["vencido"]:
                estado = "disable"
                texto = f"{hollow['nombre']} (vencido)"
            elif  i == 0 or self.hollows[i-1]["vencido"]:
                estado = "normal"
                texto = f"{hollow['nombre']}"
            else:
                estado = "disable"
                texto = f"{hollow['nombre']}"
            
            boton = tk.Button(self, text=texto, state=estado, command=lambda h=hollow: self.iniBatalla(h))
            boton.pack(pady=5) 