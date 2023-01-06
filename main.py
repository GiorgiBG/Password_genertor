import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    # list of all symbols which I generated above
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    # list to string
    password_string = "".join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password_string)
    # clearing clipboard
    window.clipboard_clear()
    window.clipboard_append(password_string)
    saved_in_clipboard_label.configure(text="Password saved in clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    pas = password_entry.get()

    # Blank field
    if len(website) == 0 and len(pas) == 0:
        messagebox.showwarning(title="Error", message="Do not leave empty fields")
    else:
        # Pop up message
        yes_save = messagebox.askokcancel(title="Save", message="Would you like to save details?")

        if yes_save:
            with open("password_entry.txt", "a") as text_file:
                text_file.write(f"website: {website}"
                                f"\nEmail: {email}"
                                f"\nPassword: {pas}\n\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                saved_in_clipboard_label.configure(text="")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
# window title
window.title("Password Generator")
# window size
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
my_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_text = tk.Label(text="Email/Username:")
email_username_text.grid(row=2, column=0)

email_username_entry = tk.Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "@gmail.com")

password = tk.Label(text="password")
password.grid(row=3, column=0)

password_entry = tk.Entry(width=24)
password_entry.grid(row=3, column=1)

password_button = tk.Button(text="Generate", command=generate_password)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

saved_in_clipboard_label = tk.Label(text="")
saved_in_clipboard_label.grid(row=5,column=1)

window.mainloop()
