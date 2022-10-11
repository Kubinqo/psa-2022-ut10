#!/user/bin/env python3

import socket
IP_SERVER = "127.0.0.1"
PORT_SERVER = 8888

class Sprava:
    def __init__(self, nick):
        self._nick = nick

    def vytvor(self, operacia, text):
        return "{}|{}|{}".format(self._nick, operacia, text).encode()

    def parsuj(self, data):
        stringData = data.decode()
        return stringData.split("|") #vrati list prvkov

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_SERVER, PORT_SERVER))

    nick = input("Zadajte nick: ")
    sprava = Sprava(nick)
    sock.send(sprava.vytvor("LOGIN", ""))

    while True:
        text = input("Zadajte spravu: ")
        sock.send(sprava.vytvor("SEND", text))

    sock.close()
    