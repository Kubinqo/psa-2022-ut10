#!/user/bin/env python3
from netmiko import ConnectHandler

IP = "158.193.152.117"
MENO = "admin"
HESLO = "Admin123"

router_param = {"device_type": "cisco_ios",
                "host": IP,
                "username": MENO,
                "password": HESLO}

if __name__ == "__main__":
    client = ConnectHandler(**router_param)
    vystup = client.send_command("sh ip int brief")
    print(vystup)

    config = [
        "int lo3005",
        "ip add 3.0.0.16 255.255.255.255"
    ]
    vystup = client.send_config_set(config)
    print(vystup)

    vystup = client.send_command("sh ip int brief")
    print(vystup)