import tkinter as tk
import os
from time import strftime

class ClockWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.bind("<ButtonPress-1>", self.start_drag)
        self.root.bind("<B1-Motion>", self.drag)
        #self.root.overrideredirect()  # Remove a barra de título da janela
        self.root.attributes("-topmost", True)  # Mantém a janela acima de outras janelas
        self.root.geometry("")  # Define a posição inicial do widget na tela

        self.horas = tk.Label(self.root, bg='#000000', fg='#ffffff', font=('Montserrat', 64, 'bold'))
        self.horas.pack()

        self.get_horas()
        self.root.bind("<ButtonRelease-1>", lambda event: self.root.config(cursor="arrow"))

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


    def get_horas(self):
        hora_atual = strftime('%H:%M:%S')
        self.horas.config(text=hora_atual)
        self.horas.after(100, self.get_horas)
    





