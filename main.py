"""
user: admin
password: C1sco12345
IP = 10.10.20.14
"""
"""
POST http://APIC-IP/api/aaaLogin.json HTTP/1.1
Content-Type: application/json

{
    "aaaUser" : {
        "attributes" : {
            "name" : "APIC_USER",
            "pwd" : "APIC_PASSWORD"
        }
    }
}

"""
import requests
import json
import conf

requests.packages.urllib3.disable_warnings()
url = "https://10.10.20.14/api/aaaLogin.json"
dato = {
    "aaaUser" : {
        "attributes" : {
            "name" : conf.usuario,
            "pwd" : conf.clave
        }
    }
}
cabecera = {"Content-Type": "application/json"}

respuesta = requests.post(url,data=json.dumps(dato),headers=cabecera,verify=False)
respuesta_json = respuesta.json()
print(respuesta_json)
Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print("\nAPI-Token: "+Token)
