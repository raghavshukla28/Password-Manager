from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# -------------------------------- CONSTANTS ------------------------------------ #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ----------------------------- RETURN PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="No Data File Found.")
        return

    if website in data:
        email = data[website]["Username"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Username: {email}\nPassword: {password}")
    elif len(website_entry.get()) == 0:
        messagebox.showinfo(title="404!", message=f"Please enter a website.")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")




# ------------------------------ SAVE PASSWORD -------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"Username": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername --> {email} \nPassword --> {password} \nReady to save?")

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Updating old data with new data
        data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(height=200, width=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=YELLOW, fg="black", font=(FONT_NAME, 12, "bold"))
website_label.grid(row=1, column=0)
email_label = Label(text="Username:", bg=YELLOW, fg="black", font=(FONT_NAME, 12, "bold"))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=YELLOW, fg="black", font=(FONT_NAME, 12, "bold"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=25)  # Adjust width as needed
website_entry.grid(row=1, column=1, pady=8, sticky='e')  # Align left
website_entry.focus()


email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, pady=8, columnspan=2)
email_entry.insert(0, "raghavshukla2628@gmail.com")


password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, padx=7, pady=8, sticky='e')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg=GREEN, fg="black", font=(FONT_NAME, 9, "bold"))
generate_password_button.grid(row=3, column=2)


add_button = Button(text="Add", width=20, command=save, bg=GREEN, fg="black", font=(FONT_NAME, 9, "bold"))
add_button.grid(row=4, column=1, columnspan=2)


search_button = Button(text="Search", command=find_password, bg=PINK, fg="black", font=(FONT_NAME, 9, "bold"))
search_button.grid(row=1, column=2, padx=10, sticky='w')  # Adjust alignment


window.mainloop()
