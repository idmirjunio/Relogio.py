from tkinter import * 

root = Tk()

def tela():
    
    root.title("Comando")
    root.config(background= "#000000")
    root.geometry()
    root.resizable()
    bob=Frame(width=50, height=60)
    bob.place(relx=0.02,rely=0.5, relheight=0.96,relwidth=0.46)
    Frame(width=50, height=60).place(relx=0.02,rely=0.5, relheight=0.96,relwidth=0.46)
    Button(bob,text="bola").place(relx=0.2,rely=0.1, relheight=0.1,relwidth=0.15)

tela()
root.mainloop()        
        