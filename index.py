# Chargement des modules
from tkinter import *
import requests
from tkinter.messagebox import *
print("Chargement des modules..")


class Bitcoine(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Bitcoin Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Bitcoin est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["BTCEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Bitcoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Bitcoins(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Bitcoin Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Bitcoin est de " +
                      str(self.getBTCPrice()) + "$")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["BTCUSDT"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Bitcoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Ethereume(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Ethereum Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix de l'Ethereum est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["ETHEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix de l'Ethereum")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Ethereums(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Ethereum Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix de l'Ethereum est de " +
                      str(self.getBTCPrice()) + "$")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["ETHUSDT"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix de l'Ethereum")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()

class Litecoine(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Litecoine Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Litecoin est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["LTCEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Litecoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()

class Litecoins(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Litecoine Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Litecoin est de " +
                      str(self.getBTCPrice()) + "$")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["LTCUSDT"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Litecoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()

class Index(Tk):

    print("Initialisation de la page d'accueil")

    def __init__(self):
        Tk.__init__(self)

        self.title("Accueil")
        self.geometry("1000x600")

        print("Page d'accueil initialisée !")

        self.window()

    def window(self):
        print("Chargement de la menubar de la page d'accueil..")
        menu = Menu(self)

        menu.add_command(label="Quitter", command=quit)
        menu.add_command(label="Bitcoin (€)", command=self.bitcoine)
        menu.add_command(label="Bitcoin ($)", command=self.bitcoins)
        menu.add_command(label="Ethereum (€)", command=self.ethereume)
        menu.add_command(label="Ethereum ($)", command=self.ethereums)
        menu.add_command(label="Litecoin (€)", command=self.litecoine)
        menu.add_command(label="Litecoin ($)", command=self.litecoins)
        
        self.config(menu=menu)
        print("Menubar de la page d'accueil chargée !")
        self.mainloop()

    def bitcoine(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Bitcoine()

    def bitcoins(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Bitcoins()

    def ethereume(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Ethereume()

    def ethereums(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Ethereums()

    def litecoine(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Litecoine()

    def litecoins(self):
        print("Lancement de la classe..")
        print("Ouverture de la page..")
        self.destroy()
        Litecoins()

print("Chargement de la page d'Accueil..")
window = Index()
print("Page d'Accueil ouverte !")