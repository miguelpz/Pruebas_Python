from config.config import *
from common.functions import *
from common.menuoptions import *

import sys
import os



creditos = ("Miguel Angel","sutia",2018)
infotweet={}
listatweet=[]


if "-v" in sys.argv:
    print ("Twitter Arles 0.1")
    sys.exit(0)

if not os.path.exists ("data/"):
    os.mkdir ("data/")

print("Bienvenido a esta aplicacion.")
login = input("Cuel es tu usuario?")
usuarios ={}



if os.path.exists (USUARIOS):
    usuarios = cargarFichero(USUARIOS)
   

if login not in usuarios.keys():
    print ("Tu usuario no existe, vamos a crearlo")
    nombre = input("Cual es tu nombre? ")
    usuarios[login] = {"id":len(usuarios)+1,"nombre":nombre}
    print (type(usuarios))
    
    escribirFichero(USUARIOS, usuarios)
    

opcion = "1"
while opcion != "5":
    if opcion not in ["1","2","3","4"]:
        print ("ERROR: Opcion incorrecta")
    print ("""Menu:
        1) Mostrar mi timeline.
        2) Escribir un nuevo tweet
        3) Seguir a un usuario
        4) Mostrar mis tweets
        5) Salir""")
    opcion = input ("Escoja una opcion: ")
    
    if opcion == "1":      
        mostrarTimeline (login, usuarios)
       
    elif opcion == "2":       
        escribirNuevoTweet (login,usuarios)
               
    elif opcion == "3":    
        seguirUsuario (login,usuarios)    
    
    elif opcion == "4":      
        mostrarMisTweets(login,usuarios)

       




        

        



        



