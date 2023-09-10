from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyperclip
import random

BACKGROUND_COLOR = "#dbd4bd"
WIDTH = 300
HEIGHT = 300

LABEL_WIDTH = 15
ENTRY_WIDTH = 45


class PasswordManager:

    def __init__(self):
        self.window = Tk()
        self.window.title("MyPass")
        self.window.minsize(300, 300)
        self.window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

        self.logo_canvas = Canvas(width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
        image = Image.open("logo.png")
        image = image.resize((200, 150))
        self.background_image = ImageTk.PhotoImage(image)
        self.logo_canvas.create_image(WIDTH / 2, HEIGHT / 2, image=self.background_image)
        self.logo_canvas.grid(row=0, column=0, columnspan=3)

        self.website_label = Label(text="Website:", width=LABEL_WIDTH, bg=BACKGROUND_COLOR)
        self.website_label.grid(row=1, column=0, pady=2)
        self.website_input = Entry(width=ENTRY_WIDTH)
        self.website_input.grid(row=1, column=1, columnspan=2, sticky=W, pady=2)

        self.email_label = Label(text="Email/Username", width=LABEL_WIDTH, bg=BACKGROUND_COLOR, )
        self.email_label.grid(row=2, column=0, pady=2)
        self.email_input = Entry(width=ENTRY_WIDTH)
        self.email_input.grid(row=2, column=1, columnspan=2, sticky=W, pady=2)

        self.password_label = Label(text="Password", width=LABEL_WIDTH, bg=BACKGROUND_COLOR)
        self.password_label.grid(row=3, column=0, pady=2)

        self.v = StringVar()
        self.password_input = Entry(width=21, textvariable=self.v)
        self.password_input.grid(row=3, column=1, sticky=W, pady=2)

        self.password_generate_button = Button(text="Generate Password", width=14, command=self.password_generator)
        self.password_generate_button.grid(row=3, column=2, sticky=E, pady=2)

        self.add_button = Button(text="Add", width=38, command=self.save_data)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)

        self.window.mainloop()

    def save_data(self):
        website = self.website_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if len(password) == 0 or len(email) == 0 or len(website) == 0:
            messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
        else:
            message = "These subscribe details entered: \nEmail: {}\nPassword: {}\nIs it ok to save?".format(email,
                                                                                                             password)
            is_ok = messagebox.askokcancel(title=f"Saving data for: {website}", message=message)
            if is_ok:
                print(self.website_input.get(), self.email_input.get(), self.password_input.get())
                with open("passwords.txt", "a") as f:
                    f.write(website + " | " + email + " | " + password + "\n")

                self.website_input.delete(0, END)
                self.password_input.delete(0, END)

    def password_generator(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)


        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_num = [random.choice(numbers) for _ in range(nr_numbers)]
        password_list = password_letters+password_symbols+password_num
        random.shuffle(password_list)

        self.password = "".join(char for char in password_list)
        self.v.set(self.password)
        pyperclip.copy(self.password)



PasswordManager()
