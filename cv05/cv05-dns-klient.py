#!/user/bin/env python3

from audioop import add
import socket as sc
import random
import struct

if __name__ == "__main__":
    sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 60000))

    transaction_id = random.randint(0, 2^16)  #generuje nahodne dvojbajtove cislo od 0 po 2^16
    flags = 0x0100                            #otazka s rekurziou
    qcount = 1                                #pocet otazok
    acount = 0                                #pocet odpovedi
    authcount = 0
    addcount = 0

    #vytvorenie dat
    data = struct.pack("!6H", transaction_id, flags, qcount, acount, authcount, addcount)
    otazka = input("Zadaj DNS meno: ")
    labels = otazka.split(".")
    
    for label in labels:
        data += struct.pack("!B", len(label))
        data += label.encode()
    
    data += struct.pack("!B", 0)              #jeden nulovy bajt - pyton neviem pracovat s mensim ako integer (4 bajty)
    data += struct.pack("!2H", 1, 1)          #1=A, 1=IN

    #posielanie dat
    sock.sendto(data, ("1.1.1.1", 53))

    #prijatie dat
    while True:
        (data,address) = sock.recvfrom(1000)
        header = data[0:12]
        (r_id, r_flags, r_questions, r_answ, r_auth, r_add) = struct.unpack("!6H", header)

        if r_id != transaction_id:
            continue
        if r_flags != 0x8180:
            continue
        if r_answ < 1:
            continue

        ipbin = data[-4:] #zaporne cislo znazornuje ze idem od konca, ak nedam za : tak ide po koniec
        ip = sc.inet_ntoa(ipbin)

        print("Odpoved od {}:{} - ip {}".format(address[0], address[1], ip))
        break

    sock.close()