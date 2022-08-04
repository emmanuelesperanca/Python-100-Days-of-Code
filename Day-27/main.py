from tkinter import *

window = Tk()
window.title('Miles to Km')
window.minsize(200, 50)
window.config(padx=40, pady=10)

# Label 1
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

# Label 2
label2 = Label(text="Km")
label2.grid(column=2, row=1)

# Label 3
label3 = Label(text="is equal to")
label3.grid(column=0, row=1)

# Label 4
label4 = Label(text="0")
label4.grid(column=1, row=1)


# Buttons 1
def action():
    value = int(entry.get()) * 1.60934
    label4.config(text=value)


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=2)

# Input
entry = Entry(width=10)

# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)

window.mainloop()
