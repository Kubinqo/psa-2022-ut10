#!/user/bin/env python3

import socket
import string

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 8888))   #port 80 iba so spravcou roota, ak by neslo tak port napr 8888
    sock.listen(1) 

    while True :
        (clientSock, clientAddr) = sock.accept()

        while True:
            data = clientSock.recv(1000) #tieto bajty su v network tvare (big endian)

            if len(data) == 0:
                break  #vyskocit z nekonecnej slucky, klient zavres spojenie
            
            try:
                stringSprava = data.decode()
            except:
                stringSprava = ""

            print("Sprava od: {}:{} - {}".format(clientAddr[0], clientAddr[1], stringSprava))

        clientSock.close()
    
    sock.close()