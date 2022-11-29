#!/user/bin/env python3

from paramiko import SSHClient, AutoAddPolicy

IP = "158.193.152.117"
MENO = "admin"
HESLO = "Admin123"

if __name__ == "__main__":
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname=IP, port=22, username=MENO, password=HESLO)
    (stdin, stdout, stderr) = client.exec_command("sh ip int brief")

    for line in stdout:
        #print(line.strip("\n"))
        riadok = line.strip("\n").strip("\r").split(" ")
        riadokBezPrazdnych = list()
        for i in riadok:
            if (i != ""):
                riadokBezPrazdnych.append(i)
        if (len(riadokBezPrazdnych) > 0):
            print("| {:16} | {:15} |".format(riadokBezPrazdnych[0], riadokBezPrazdnych[1]))

    client.exec_command("conf t")
    client.exec_command("int lo3000")
    client.exec_command("ip add 30.0.0.0 255.255.255.255")
    client.close()