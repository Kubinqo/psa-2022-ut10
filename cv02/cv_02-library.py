#!/usr/bin/env python3


class Book:
    #konstruktor
    def __init__(self, nazov, strany, autor):
        #atributy
        self._nazov = nazov
        self._strany = strany
        self._autor = autor
    
    #metoda
    def print(self):
        print("| {:20} | {:4}s | {:15} |".format(self._nazov, self._strany, self._autor))

class Library:
    def __init__(self):
        self._kniznica = list()

    def addBook(self):
        nazov = input("Zadaj nazov knihy: ")
        strany = input("Zadaj pocet stran: ")
        autor = input("Zadaj priezvisko autora: ")

        kniha = Book(nazov, strany, autor)
        self._kniznica.append(kniha)

    def print(self):
        print("| {:20} | {:4} | {:15} |".format("NAZOV", "STRANY", "AUTOR"))
            
        # klasicky for /for i in range(0,10):/

        #foreach
        for book in self._kniznica:
            book.print()

    def seed(self):
        self._kniznica.append(Book("Hobbit", 350, "Tolkien"))    
        self._kniznica.append(Book("CCNA", 2000, "Cisco"))
        self._kniznica.append(Book("Python", 100, "KIS FRI"))

    def menu(self):
        print("0 - Pridaj knihu")
        print("1 - Vypis kniznicu")
        print("q - ukonci program")

        volba = input("Vyber si moznost(0-1, q): ")

        if volba == "0":
            self.addBook()
        elif volba == "1":
            self.print()
        else:
            exit()

    def banner(self):
        print("Book library, version 0.1a0")
        #prazdny riadok
        print()

if __name__ == "__main__":
    kniznica = Library()
    kniznica.seed()
    kniznica.banner()

    while True:
        kniznica.menu()


