#!/user/bin/env python3

from paramiko import SSHClient, AutoAddPolicy

IP = "158.193.152.78"
MENO = "admin"
HESLO = "Admin123"

if __name__ == "__main__":
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname=IP, port=22, username=MENO, password=HESLO)

    client.exec_command("/ip address add address=3.0.0.1/32 interface=lo0")

    (stdin, stdout, stderr) = client.exec_command("/ip address print terse")

    for line in stdout:
        riadok = line.strip("\n").strip("\r").split(" ")
        riadokDict = dict()
        for i in riadok:
            prvok = i.split("=")
            if (len(prvok) >= 2):
                riadokDict[prvok[0]] = prvok[1]
        print(riadokDict)

    client.close()