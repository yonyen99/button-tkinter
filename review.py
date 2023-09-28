import tkinter as tk
window = tk.Tk()
window.title("Button")
window.geometry("400x400")

frame = tk.Frame(window, width=350, height=550)
frame.pack()

canvas = tk.Canvas(frame, width=100, height=50)
canvas.pack()

rectangle = canvas.create_rectangle(20, 20, 100, 100, fill="orange")

def colorOrange():
    canvas.itemconfig(rectangle, fill='orange')

def colorBlue():
    canvas.itemconfig(rectangle, fill='blue')

buttonOrange = tk.Button(frame, text="orange", command=colorOrange)
buttonOrange.pack()

buttonBlue = tk.Button(frame, text="blue", command=colorBlue)
buttonBlue.pack()

window.mainloop()
