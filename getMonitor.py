"""
GET https://apic-ip-address/api/node/class/faultInst.xml?query-target-filter=and(eq(faultInst.cause,"config-failure"))
"""
import requests
import json
import conf

def pedir_token():

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

    respuesta = requests.post(url, data=json.dumps(dato), headers=cabecera,verify=False)
    respuesta_json = respuesta.json()
    #print(respuesta_json)
    Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    #print("\nAPI-token: "+Token)
    return Token

API_Token = pedir_token()
#print("\nAPI_Token: "+API_Token)
print("&"*70)

url =  "https://10.10.20.14/api/node/class/faultInst.json"
cabecera = {"Content-Type": "application/json"}
cookie = {"APIC-cookie": API_Token}

respuesta = requests.get(url,headers=cabecera,cookies=cookie,verify=False)
respuesta_json = respuesta.json()
#print (respuesta_json)

#respuesta_json["imdata"][0]["faultInst"]["attributes"]["severity"]

for i in range(0,814):
    created = respuesta_json["imdata"][i]["faultInst"]["attributes"]["created"]
    severity = respuesta_json["imdata"][i]["faultInst"]["attributes"]["severity"]
    code = respuesta_json["imdata"][i]["faultInst"]["attributes"]["code"]
    type = respuesta_json["imdata"][i]["faultInst"]["attributes"]["type"]
    cause = respuesta_json["imdata"][i]["faultInst"]["attributes"]["cause"]
    if respuesta_json["imdata"][i]["faultInst"]["attributes"]["severity"] == 'warning':
        print("Fecha/Hora: " +created+"     "+"Severidad: " +severity+"     "+"Código: "+code+"     "+"Tipo: "+type+"     "+"Causa: "+cause)

