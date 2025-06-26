

from usuario import Usuario
import datetime
import json
import pytz
#import requests #para capturar json que vienen de internet
"""
ruta = "usuario.txt" #se puede colocra de sta forma tambien 
with open(ruta)
"""
tz_CL = pytz.timezone("America/Santiago")
datetime_CL = datetime.datetime.now(tz_CL)



instancias = []

with open("usuarios.txt") as u:
    linea = u.readline()
    while linea:
        try:
            usuario = json.loads(linea)  ## loads se utiliza para cargar datos json desde una caden string y convertiro en un objeto natvo de python
            instancias.append(Usuario(
                usuario.get("nombre"),
                usuario.get("apellido"),
                usuario.get("email"),
                usuario.get("genero")
            ))
            
        except Exception as e:
            with open("error.log","a+") as log:
                log.write(f"{datetime_CL.strftime("%d/%m/%Y, %H:%M:%S")}, {e} \n")

        finally:
            linea = u.readline()

print(instancias)




