#!/user/bin/env python3

import urllib.request as ur
import xml.etree.ElementTree as ET
import tkinter as tk

RSS_URL = "http://www.dsl.sk/export/rss_articles.php"

def parsujRSS(url):
    spojenie = ur.urlopen(url)
    page = spojenie.read()
    
    vystup = list()
    root = ET.fromstring(page)
    for channel in root:
        for item in channel:
            if (item.tag == "item"):
                for i in item:
                    clanok = ""
                    for i in item:
                        if (i.tag == "title"):
                            clanok += i.text + " | "
                        if (i.tag == "link"):
                            clanok += i.text
                    vystup.append(clanok)
    return vystup    

def vytvorGUI():
    okno = tk.Tk()
    nastavGUI(okno)

    okno.mainloop()      

def nastavGUI(okno):
    okno.title("RSS Parser")
    okno.geometry("800x400+400+200")
    #okno.resizable(True,False)
    
    labelURL = tk.Label(okno, text="Url")
    labelURL.grid(row=0, column=0, sticky="w", padx=5)

    entryURL = tk.Entry(okno)
    entryURL.grid(row=0, column=1, ipadx=200)
    entryURL.insert(0, RSS_URL)

    buttonURL = tk.Button(okno, text="Parsuj", command=lambda: obsluzButton(entryURL.get(), text))
    buttonURL.grid(row=0, column=2, ipadx=5)

    text = tk.Text(okno)
    text.grid(row=1, column=0, columnspan=3, padx=5)

def obsluzButton(url, textArea):
    textArea.delete("1.0", tk.END)
    vystup = parsujRSS(url)
    for i in vystup:
        textArea.insert(tk.END, i+"\n")

if __name__ == "__main__":
    #vystup = parsujRSS(RSS_URL)
    #print(vystup)
    vytvorGUI()