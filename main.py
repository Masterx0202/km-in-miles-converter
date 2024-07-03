import tkinter as tk
import ttkbootstrap as bttk
from tkinter import ttk



# Create the main window
window = bttk.Window(themename = "darkly")
window.title("converter")
window.geometry("300x150")

#convert
def convert():
    output.set(input_value.get() * 0.621371)
    return output

#tile
title_label = tk.Label(window, text="miles to kilometers", font = "Arial 15 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(window)
input_value = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable = input_value)
button = ttk.Button(input_frame, text = "convert", command = convert)
entry.pack(side="left", padx = 10)
button.pack(side="left", padx = 10)
input_frame.pack()


#output
output = tk.StringVar()
output_label = ttk.Label(
    window,
    text = "output",
    font = "Arial 15",
    textvariable = output)
output_label.pack()


#main run 
window.mainloop()