from Tkinter import *
import webbrowser
import os
#from googlesearch import *

root = Tk()
root.title("Menu")
#root.geometry('745x120')
root.resizable(width=0, height=0)
#def search():
#	query = wyszukaj.get()
#	webbrowser.get('firefox').open('https://google.com/search?q=%s' % query)
def center_window(width=745, height=120):
    # get screen width and height
    	screen_width = root.winfo_screenwidth()
    	screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    	x = (screen_width/2) - (width/2)
   	y = (screen_height/2) - (height/2)
    	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window(745, 120)
def weather():
	webbrowser.open('https://www.twojapogoda.pl/')
def info():
	webbrowser.open('https://echodnia.eu/swietokrzyskie/wiadomosci/wloszczowa/')
def wylacz():
	os.system("shutdown now")
def inter():
	webbrowser.open('https://google.com')

#wyszukaj = Entry(root, width="92", borderwidth="5")
#wysz_Button = Button(root, text="Wyszukaj", command=search, padx=92)
internet = Button(root, text="Internet", command=inter, padx=65, pady=50)
pogoda = Button(root, text="Pogoda", command=weather, padx=66, pady=50)
wiadomosci = Button(root, text="Wloszczowa", command=info, padx=50, pady=50)
wylacz = Button(root, text="Wylacz", command=wylacz, padx=67, pady=50)

#wyszukaj.grid(row=0, column=0, columnspan=4)
#wysz_Button.grid(row=1, column=0, columnspan=4)
internet.grid(row=2, column=1)
pogoda.grid(row=2,column=2)
wiadomosci.grid(row=2,column=3)
wylacz.grid(row=2,column=0)

root.mainloop()
