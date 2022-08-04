import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    entry_password.delete(0, END)

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, string=f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Ooops...', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reads old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updates old data into a new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saves the new updated data into the json file
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = entry_website.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password} ')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=0, row=0, columnspan=3)

# Website
website_label = Label(text="Website", font=('Arial', 8, 'normal'))
website_label.grid(column=0, row=1)

# Email/Username
email_label = Label(text="Email/Username", font=('Arial', 8, 'normal'))
email_label.grid(column=0, row=2)

# Password
password_label = Label(text="Password", font=('Arial', 8, 'normal'))
password_label.grid(column=0, row=3)

# Entry of Website
entry_website = Entry(width=32)
entry_website.grid(column=1, row=1, columnspan=1)
entry_website.focus()

# Entry of Email/Username
entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan=2)

# Entry of Password
entry_password = Entry(width=32)
entry_password.grid(column=1, row=3, columnspan=1)

# Generate Password Button
password_button = Button(text="Generate Password", command=generate)
password_button.grid(column=2, row=3, columnspan=1)

# Add Button
add_button = Button(text="Add", command=add, width=43)
add_button.grid(column=1, row=4, columnspan=2)

# Search Button
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()
