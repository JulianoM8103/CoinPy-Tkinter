# Docs : https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
# import des différents modules
from tkinter import * 
from tkinter.messagebox import *
import json
import requests

# Boucles et variables

def quit():
    print("Confirmation de la fermeture de la fenêtre..")
    res = askyesno("Attention", "Êtes vous sûr de quitter l'application ?")
    if res == True:
        fenetre.destroy()
    
def bitcoine():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["BTCEUR"]
    j = 0
    for i in currencies:
     url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j+1
    print("Le prix du Bitcoin est de",data['price'],"€")
    bitcoine = data['price']

    bitcoinpricee = Tk()
    bitcoinpricee.title("Prix du Bitcoin en € - CoinPy")
    label = Label(bitcoinpricee, textvariable=data['price'])
    label.pack()
    label = Label(bitcoinpricee, text="Test")
    label.pack()
    fenetre.destroy()
    bitcoinpricee.mainloop()

def bitcoins():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["BTCUSDT"]
    j = 0
    for i in currencies:
     url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j+1
    print("Le prix du Bitcoin est de",data['price'],"$")

def ethereume():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["ETHEUR"]
    j = 0
    for i in currencies:
     url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j+1
    print("Le prix de l'Ethereum est de",data['price'],"€")

def ethereums():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["ETHUSDT"]
    j = 0
    for i in currencies:
     url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j+1
    print("Le prix de l'Ethereum est de",data['price'],"$")

# ouverture de la fenêtre
fenetre = Tk()
fenetre.title("CoinPy")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Bitcoin (€)", command=bitcoine)
menu1.add_command(label="Bitcoin ($)", command=bitcoins)
menu1.add_separator()
menu1.add_command(label="Ethereum (€)", command=ethereume)
menu1.add_command(label="Ethereum ($)", command=ethereums)
menu1.add_separator()
menu1.add_command(label="Quitter", command=quit)
menubar.add_cascade(label="Cryptomonnaies", menu=menu1)

fenetre.config(menu=menubar)
fenetre.mainloop()