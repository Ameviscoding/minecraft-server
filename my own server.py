from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("The Server App")
window.geometry("800x600")
window.resizable(True,True)
font_header = ('Arial',15)
font_entry = ('Arial',12)
font_label = ('Arial',11)
base_padding = {'padx':10,'pady':8}
header_padding = {'padx':10,'pady':12}
def clicked():
    username = username_entry.get()
    password = password_entry.get()
    avatar = avatar.load()
    messagebox.showinfo('''Welcome to the car server. Here you can think of a car and get the resources for the car that you are thinking of.
                        So the first thing is that you will be put into creative mode so that you can see the resources and how they look like.
                        Then you can go into survival and go caveing and because you know how they look like you can mine the ore with a iron picaxe or
                        above and the crafting recipies will be in the crafting book. Enjoy!''',{username},{password})
main_label = Label(window,text = 'The car server',font = font_header,justify = CENTER)
main_label.pack()
username_label = Label(window,text = 'login',font = label_font)
username_label.pack()
password_label = Label(window,text = 'password',font = label_font)
username_entry = Entry(window,bg = '#00ff00',tg = '#000000',bg = '#0000ff')
