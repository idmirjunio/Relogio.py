import tkinter as tk
from widget import ClockWidget
import sys

if sys.executable.endswith("pythonw.exe"):
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")

root = tk.Tk()
root.title('Meu Relógio')

clock_widget = ClockWidget(root)
clock_widget.pack()

root.mainloop()