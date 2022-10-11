#!/user/bin/env python3

import socket

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 8888))   #port 80 iba so spravcou roota, ak by neslo tak port napr 8888
    sock.listen(1) 

    sprava = Sprava("server")

    while True :
        (clientSock, clientAddr) = sock.accept()

        while True:
            data = clientSock.recv(1000) #tieto bajty su v network tvare (big endian)

            if len(data) == 0:
                break  #vyskocit z nekonecnej slucky, klient zavres spojenie
            
            try:
                zoznam = sprava.parsuj(data)
                if zoznam[1] == "LOGIN":
                    print("Prihlasil sa klient" + zoznam[0])
                    continue
                elif zoznam[1] == "SEND":
                    print("Sprava od: {}: {}".format(zoznam[0], zoznam[2]))
            except:
                continue

        clientSock.close()
    
    sock.close()