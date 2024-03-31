from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(web_name, email, password):
    new_data = {
        web_name: {
            "Email": email,
            "Password": password
        }
    }
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        web_entry_box.delete(0, END)
        email_entry_box.delete(0, END)
        email_entry_box.insert(0, "sanjana@gmail.com")
        web_entry_box.focus()
        password_box.delete(0, END)


def on_add():
    web_name = web_entry_box.get()
    email = email_entry_box.get()
    password = password_box.get()

    if web_name == "" or password == "":
        messagebox.showwarning(title="Something went Wrong ", message="You left some fields empty!!!")
    else:
        is_ok = messagebox.askokcancel(title=web_name,
                                       message=f"Email: {email}\nPassword: {password}\nIs it okay to SAVE ?")

        if is_ok:
            save(web_name, email, password)
        else:
            web_entry_box.delete(0, END)
            email_entry_box.delete(0, END)
            email_entry_box.insert(0, "sanjana@gmail.com")
            web_entry_box.focus()
            password_box.delete(0, END)


# ---------------------------- SEARCH PASSWORDS ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = web_entry_box.get()
            email = data[website]["Email"]
            password = data[website]["Password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data is Added!")
    except KeyError:
        messagebox.showinfo(title="Error", message="This data doesn't Exist! \nor maybe a spell mistake")
    else:
        messagebox.showinfo(title=website, message=f"   For {website}\nEmail: {email}\nPassword: {password}")
    finally:
        web_entry_box.delete(0, END)
        web_entry_box.focus()
        password_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
image = PhotoImage(file='logo.png')

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=("Arial", 15, "bold"))
web_label.grid(row=1, column=0)
web_entry_box = Entry(width=21)
web_entry_box.focus()
web_entry_box.grid(row=1, column=1)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", font=("Arial", 15, "bold"))
email_label.grid(row=2, column=0)
email_entry_box = Entry(width=37)
email_entry_box.insert(0, "sanjana@gmail.com")
email_entry_box.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 15, "bold"))
password_label.grid(row=3, column=0)
password_box = Entry(width=22)
password_box.grid(row=3, column=1)
generate_button = Button(text="Generate Password", width=13, font=("Areal", 12), command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, height=2, command=on_add, bg="white", activebackground="blue")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
