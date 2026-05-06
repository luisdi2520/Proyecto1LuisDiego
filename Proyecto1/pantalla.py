import tkinter as tk
from tkinter import messagebox

class PantallaInicio(tk.Frame):
    def __init__(self, master, personajes, inicio):
        super(). __init__(master)
        self.master = master
        self.personajes = personajes
        self.inicio = inicio

        self.avatar_selecc = tk.StringVar(value="Avatar1")
        self.pantalla()
    
    def pantalla(self):
        label = tk.Label(self, text="Disney Epic Adventure", font=("Arial", 20, "bold"))
        label.pack()

        #Nombre del jugador
        nombre = tk.Label(self, text="Ingrese nombre:")
        nombre.pack()
        self.entry_nombre =  tk.Entry(self)
        self.entry_nombre.pack(pady= 5)

        #seleccion
        seleccion = tk.Label(self, text= "seleccione a 3 personajes:")
        seleccion.pack()
        self.listbox = tk.Listbox(self, selectmode=  tk.MULTIPLE, height=15)
        for p in  self.personajes:
            self.listbox.insert(tk.END, p["nombre"])
        self.listbox.pack(pady=5)


        #seleccion de avatar
        avatar = tk.Label(self, text="Selecione AVatar:")
        avatar.pack()
        for avatar in ["Avatar1", "Avatar2", "Avatar3"]:
            avatar_button = tk.Radiobutton(self, text= avatar, variable= self.avatar_selecc, value=avatar)
            avatar_button.pack()
        
        #botones
        inicio = tk.Button(self, text="Inicio", command=self.iniciar)
        inicio.pack(pady=10)
        about = tk.Button(self, text="About", command=self.about)
        about.pack()
    
    def iniciar(self):
        nombre = self.entry_nombre.get().strip()
        seleccionados = self.listbox.curselection()

        if nombre == "":
            messagebox.showerror("Error", "debes ingresar tu nombre.")
            return
        if len(seleccionados) != 3:
            messagebox.showerror("Error", "debes escoger 3 personajes")
            return 
        equipo =[self.personajes[i] for i in seleccionados]
        avatar = self.avatar_selecc.get()

        self.inicio(nombre, equipo, avatar)

    def about(self):
         sobre ='''Disney's Epic Adventure 
        Creador: Luis Diego Murillo Matarrita
        Version: 1.0'''
         messagebox.showinfo("About", sobre)


