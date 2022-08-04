from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
to_learn = {}
# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_word():
    global random_word
    global timer
    window.after_cancel(timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(data_text, text=f"{random_word['French']}", fill='black')
    canvas.itemconfig(language_text, text="French", fill='black')
    canvas.itemconfig(canvas_image, image=front_photo)
    timer = window.after(3000, func=translation)


def translation():
    canvas.itemconfig(data_text, text=f"{random_word['English']}", fill='white')
    canvas.itemconfig(language_text, text="English", fill='white')
    canvas.itemconfig(canvas_image, image=back_photo)


def in_known():
    to_learn.remove(random_word)
    data = pd.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn.csv', index=False)
    next_word()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title('FlashCard')
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
timer = window.after(3000, func=translation)

# Front Image
front_photo = PhotoImage(file='./images/card_front.png')
# Back Image
back_photo = PhotoImage(file='./images/card_back.png')

canvas_image = canvas.create_image(400, 263, image=front_photo)
canvas.grid(column=0, row=0, columnspan=2)

# Right button
right_photo = PhotoImage(file='./images/right.png')
button = Button(text="Start", image=right_photo, command=in_known)
button.grid(column=1, row=1)

# Wrong button
wrong_photo = PhotoImage(file='./images/wrong.png')
button = Button(text="Start", image=wrong_photo, command=next_word)
button.grid(column=0, row=1)

# Texts
language_text = canvas.create_text(400, 163, text='Title', fill='black', font=('Ariel', 25, 'italic'))
data_text = canvas.create_text(400, 263, text=f'Word', fill='black', font=('Ariel', 45, 'bold'))

next_word()
window.mainloop()
