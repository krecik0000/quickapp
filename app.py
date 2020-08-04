from Tkinter import *
import tkFont
import webbrowser
import os
#from googlesearch import *

root = Tk()
root.title("Menu")
root.configure(bg='#2b2b2b')
#root.geometry('745x120')
root.resizable(width=0, height=0)
def center_window(width=745, height=120):
    	screen_width = root.winfo_screenwidth()
    	screen_height = root.winfo_screenheight()
    	x = (screen_width/2) - (width/2)
   	y = (screen_height/2) - (height/2)
    	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window(560, 320)
font = tkFont.Font(size=25)
def weather():
	webbrowser.open('https://www.twojapogoda.pl/')
def info():
	webbrowser.open('https://echodnia.eu/swietokrzyskie/wiadomosci/wloszczowa/')
def wylacz():
	os.system("shutdown now")
def inter():
	webbrowser.open('https://google.com')
internet = Button(root, text="Internet", command=inter, padx=70, pady=50, bg='#2b2b2b', fg='#fff', font=font)
pogoda = Button(root, text="Pogoda", command=weather, padx=75, pady=50, bg='#2b2b2b', fg='#fff', font=font)
wiadomosci = Button(root, text="Wloszczowa", command=info, padx=37, pady=50, bg='#2b2b2b', fg='#fff', font=font)
wylacz = Button(root, text="Wylacz", command=wylacz, padx=78, pady=50, bg='#2b2b2b', fg='#fff', font=font)
bo = Label(root, text="Biuro Obslugi Klienta: Milosz", pady=5, fg='#fff', bg='#2b2b2b')

internet.grid(row=1, column=0)
pogoda.grid(row=1,column=1)
wiadomosci.grid(row=2,column=0)
wylacz.grid(row=2,column=1)
bo.grid(row=3,column=0, columnspan=2)

root.mainloop()
