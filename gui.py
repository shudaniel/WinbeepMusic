import tkinter as tk

window = tk.Tk()
buttonC = tk.Button(
    text="C",
    width=25,
    height=5,
)

buttonD = tk.Button(
    text="D",
    width=25,
    height=5,
)

buttonE = tk.Button(
    text="E",
    width=25,
    height=5,
)

buttonF = tk.Button(
    text="F",
    width=25,
    height=5,
)

buttonG = tk.Button(
    text="G",
    width=25,
    height=5,
)

buttonA = tk.Button(
    text="A",
    width=25,
    height=5,
)

buttonB = tk.Button(
    text="B",
    width=25,
    height=5,
)

buttonHighC = tk.Button(
    text="High C",
    width=25,
    height=5,
)

buttonC.grid(row=0, column=0)
buttonD.grid(row=0, column=1)
buttonE.grid(row=0, column=2)
buttonF.grid(row=1, column=0)
buttonG.grid(row=1, column=1)
buttonA.grid(row=1, column=2)
buttonB.grid(row=2, column=0)
buttonHighC.grid(row=2, column=1)
window.mainloop()