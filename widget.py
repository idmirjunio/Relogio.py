import tkinter as tk
import os
from time import strftime

class ClockWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.bind("<ButtonPress-1>", self.start_drag)
        self.root.bind("<B1-Motion>", self.drag)
        self.root.overrideredirect(True)  # Remove a barra de título da janela
        self.root.attributes("-topmost", True)  # Mantém a janela acima de outras janelas
        self.root.geometry("+100+100")  # Define a posição inicial do widget na tela

        self.light = tk.PhotoImage(file='brightness.png')
        self.dark = tk.PhotoImage(file='dark.png')

        self.dark_mode_button = tk.Button(self.root, command=self.toggle_dark_mode)
        self.dark_mode_button.config(image=self.dark, bd=0, bg='#1d1d1d')
        self.dark_mode_button.pack(pady=10)

        self.tela = tk.Canvas(self.root, width=600, height=20, bg='#1d1d1d', bd=0, highlightthickness=0,
                              relief='ridge')
        self.tela.pack()

        self.saudacao = tk.Label(self.root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
        self.saudacao.pack()

        self.data = tk.Label(self.root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
        self.data.pack()

        self.horas = tk.Label(self.root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 64, 'bold'))
        self.horas.pack()

        self.get_saudacao()
        self.get_data()
        self.get_horas()

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


    def toggle_dark_mode(self):
        if self.root['bg'] == '#1d1d1d':
            self.root['bg'] = 'white'
            self.tela['bg'] = 'white'
            self.saudacao['bg'] = 'white'
            self.data['bg'] = 'white'
            self.horas['bg'] = 'white'
            self.dark_mode_button['image'] = self.light
            self.dark_mode_button['bg'] = 'white'
        else:
            self.root['bg'] = '#1d1d1d'
            self.tela['bg'] = '#1d1d1d'
            self.saudacao['bg'] = '#1d1d1d'
            self.data['bg'] = '#1d1d1d'
            self.horas['bg'] = '#1d1d1d'
            self.dark_mode_button['image'] = self.dark
            self.dark_mode_button['bg'] = '#1d1d1d'

    def get_saudacao(self):
        nome_usuario = os.getlogin()
        self.saudacao.config(text='Olá, ' + nome_usuario)

    def get_data(self):
        data_atual = strftime('%a, %d %b %Y')
        self.data.config(text=data_atual)

    def get_horas(self):
        hora_atual = strftime('%H:%M:%S')
        self.horas.config(text=hora_atual)
        self.horas.after(100, self.get_horas)
