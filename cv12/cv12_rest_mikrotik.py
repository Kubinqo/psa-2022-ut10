#!/user/bin/env python3
import requests
from flask import Flask, render_template, request

IP = "158.193.152.78"
MENO = "admin"
HESLO = "Admin123"

app = Flask(__name__)

def vypisRozhrania():
    odpoved = requests.get("https://{}/rest/interface".format(IP), auth=(MENO, HESLO), verify=False)
    if (odpoved.status_code == 200):
        vystup = list()
        for rozhranie in odpoved.json():
            vystup.append({"id": rozhranie.get(".id"), "name": rozhranie.get("name")})
        return vystup
    else:
        return None

def vytvorLoopback(nazov_loop):
    telo = {"name": nazov_loop}
    odpoved = requests.put("https://{}/rest/interface/bridge".format(IP), auth=(MENO, HESLO), verify=False, json=telo)
    print(odpoved.text)
    if (odpoved.status_code == 201):
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST"):
        nazov_loop = request.form["nazov"]
        vytvorLoopback(nazov_loop)

    data =  vypisRozhrania()
    return render_template("index.html", rozhrania=data)

if __name__ == "__main__":
    #vytvorLoopback("lo-Henry")
    #print(vypisRozhrania())
    app.run(host="0.0.0.0", port=8888)