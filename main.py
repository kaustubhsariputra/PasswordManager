from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#------------------------------------------- PASSWORD_GENERATOR------------------------------------------
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password) #to copy password on clipboard
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, f"{password}")



#-------------------------------------- SAVE_PASSWORD----------------------------------------------------
def save_pass():


    websitedata = website_entry.get()
    passworddata = password_entry.get()
    emaildata = email_entry.get()
    new_data ={                                                       #neseted dictionary
        websitedata:{
            "email:": emaildata,
            "password:": passworddata
        }
    }
    if len(websitedata) ==0 or len(passworddata)==0 or len(emaildata)==0:
        messagebox.showerror(title="OOPS!!", message="Please fill all the details")
    else:
        is_ok = messagebox.askokcancel(title=websitedata, message=f"password is:{passworddata}\n Email is:{emaildata}\n Is it OK to Save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading Old file
                    data = json.load(data_file)
            except FileNotFoundError:
                #writing new data
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updating old data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------------------FIND PASSWORD----------------------------------------------------

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found!!")
    else:
        if website in data:
            email = data[website]["email:"]
            password = data[website]["password:"]
            messagebox.showinfo(title= website, message= f" Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="ERROR!!", message=f" Data for {website} does not exist!! ")

#---------------------------------UI_SETUP---------------------------------------------------------------
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx = 20, pady = 20)
window.minsize(width= 400, height=400)

canvas = Canvas(height =200, width = 200)
my_pass_logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = my_pass_logo )
canvas.grid(column = 1, row=0)

website_lable = Label(text= "Wbsite:")
website_lable.grid(column = 0, row = 1)

website_entry = Entry(width = 25)
website_entry.grid(column = 1, row =1)
website_entry.focus() #it will focus cursor into webiste entry


search_button = Button(text ="SEARCH", width = 12, command = find_password)
search_button.grid(column = 2, row = 1)

email_label = Label(text ="Email/User Name:")
email_label.grid(column = 0, row = 2)


email_entry = Entry(width = 47)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, "kaustubh@gmail.com")


password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)


password_entry = Entry(width = 25)
password_entry.grid(column = 1, row = 3)


generate_button = Button(text = "GENERATE PASSWORD", command = generate_password)
generate_button.grid(column = 2, row = 3)


add_button = Button(text = "ADD", width =40, command = save_pass)
add_button.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()
