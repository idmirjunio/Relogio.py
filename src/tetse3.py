import tkinter as tk

class FloatingWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.geometry("800x400+300+100")
        self.minsize(200, 200)
        self.config(bg="green")
        self.grid_columnconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=3)

        self.menu()
        self.textbox()        

        self.grip_se = tk.Label(self,bg='blue')
        self.grip_se.place(relx=1.0, rely=1.0, anchor="se")
        self.grip_se.bind("<B1-Motion>",lambda e, mode='se':self.OnMotion(e,mode))

        self.grip_e = tk.Label(self,bg='green')
        self.grip_e.place(relx=1.0, rely=0.5, anchor="e")
        self.grip_e.bind("<B1-Motion>",lambda e, mode='e':self.OnMotion(e,mode))
        
        self.grip_ne = tk.Label(self,bg='blue')
        self.grip_ne.place(relx=1.0, rely=0, anchor="ne")
        self.grip_ne.bind("<B1-Motion>",lambda e, mode='ne':self.OnMotion(e,mode))

        self.grip_n = tk.Label(self,bg='green')
        self.grip_n.place(relx=0.5, rely=0, anchor="n")
        self.grip_n.bind("<B1-Motion>",lambda e, mode='n':self.OnMotion(e,mode))

        self.grip_nw = tk.Label(self,bg='blue')
        self.grip_nw.place(relx=0, rely=0, anchor="nw")
        self.grip_nw.bind("<B1-Motion>",lambda e, mode='nw':self.OnMotion(e,mode))

        self.grip_w = tk.Label(self,bg='green')
        self.grip_w.place(relx=0, rely=0.5, anchor="w")
        self.grip_w.bind("<B1-Motion>",lambda e, mode='w':self.OnMotion(e,mode))

        self.grip_sw = tk.Label(self,bg='blue')
        self.grip_sw.place(relx=0, rely=1, anchor="sw")
        self.grip_sw.bind("<B1-Motion>",lambda e, mode='sw':self.OnMotion(e,mode))

        self.grip_s = tk.Label(self,bg='green')
        self.grip_s.place(relx=0.5, rely=1, anchor="s")
        self.grip_s.bind("<B1-Motion>",lambda e, mode='s':self.OnMotion(e,mode))

    def menu(self):
        self.frame = tk.Frame(self, height=25, bg='black')
        self.frame.grid(row=0, column=0, sticky="new")
        color = ['#FEF3B3','#FFF9DC', "#341C09"]

        for i in range(3):
            self.button = tk.Button(self.frame, text="Can you see", font=('calibri',12), bg=color[i-1], fg="red", relief="flat", bd=0)
            self.button.pack(side="left", fill="both", padx=3)
            self.lbl_space  = tk.Label(self.frame ,text="",bd=0,bg="black")
            self.lbl_space.pack(side="left", padx=5)

            self.button = tk.Button(self.frame, text="Can you see", font=('calibri',12), bg=color[i-1], fg="red", relief="flat", bd=0)
            self.button.pack(side="right", fill="both", padx=3)

            
    def textbox(self):
        self.frame2 = tk.Frame(self, bg='white')
        self.frame2.grid(row=1, column=0, sticky="wens")
        self.text_editor = tk.Text(self.frame2, wrap='word', font='calibri 12',undo = True, relief=tk.FLAT,bg="white")
        self.yscrollbar = tk.Scrollbar(self.frame2, command=self.text_editor.yview)
        self.yscrollbar.grid(row=0, column=1, sticky="ns")#ns

        self.text_editor.config(yscrollcommand=self.yscrollbar.set)
        self.text_editor.grid(row=0, column=0, sticky="wens", padx=3)

        self.frame2.grid_columnconfigure(0, weight=3)
        self.frame2.grid_rowconfigure(0, weight=3)
        self.text_editor.insert("1.0", 'Bed sincerity yet therefore forfeited his certainty neglected questions. Pursuit chamber as elderly amongst on. Distant however warrant farther to of. My justice wishing prudent waiting in be. Comparison age not pianoforte increasing delightful now. Insipidity sufficient dispatched any reasonably led ask. Announcing if attachment resolution sentiments admiration me on diminution. ')

        # insert a widget inside the text box
        options = ["choice 1","choice 2"]
        clicked = tk.StringVar()
        clicked.set(options[0])
        self.drop = tk.OptionMenu(self.text_editor, clicked, *options)
        self.text_editor.window_create("1.0", window=self.drop)
        self.drop.config(bg="#474747", relief='flat', font=('calibri',11, 'bold'))

    def OnMotion(self, event, mode):
        self.update() # <==== if you deactivate this line you can see the performance issues
        
        abs_x = self.winfo_pointerx() - self.winfo_rootx()
        abs_y = self.winfo_pointery() - self.winfo_rooty()
        width = self.winfo_width()
        height= self.winfo_height()
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        
        if mode == 'se' and abs_x >0 and abs_y >0:
                self.geometry("%sx%s" % (abs_x,abs_y)
                              )
                
        if mode == 'e':
            self.geometry("%sx%s" % (abs_x,height)
                          )
        if mode == 'ne' and abs_x >0:
                y = y+abs_y
                height = height-abs_y
                if height >0:
                    self.geometry("%dx%d+%d+%d" % (abs_x,height,
                                                   x,y))
        if mode == 'n':
            height=height-abs_y
            y = y+abs_y
            if height >0 and width >0:
                self.geometry("%dx%d+%d+%d" % (width,height,
                                               x,y))
            
        if mode == 'nw':
            width = width-abs_x
            height=height-abs_y
            x = x+abs_x
            y = y+abs_y
            if height >0 and width >0:
                self.geometry("%dx%d+%d+%d" % (width,height,
                                               x,y))
        if mode == 'w':
            width = width-abs_x
            x = x+abs_x
            if height >0 and width >0:
                self.geometry("%dx%d+%d+%d" % (width,height,
                                               x,y))
        if mode == 'sw':
            width = width-abs_x
            height=height-(height-abs_y)
            x = x+abs_x
            if height >0 and width >0:
                self.geometry("%dx%d+%d+%d" % (width,height,
                                               x,y))
        if mode == 's':
            height=height-(height-abs_y)
            if height >0 and width >0:
                self.geometry("%dx%d+%d+%d" % (width,height,
                                               x,y))
            


app=FloatingWindow()
app.mainloop()