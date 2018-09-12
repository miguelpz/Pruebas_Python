from twitter.tweets.listar import flistatweets
from twitter.tweets.pedir import pedirtweet
import os
import sys
import json

creditos = ("Miguel Angel","sutia",2018)
infotweet={}
listatweet=[]
SEGUIDORES = "data/follow.json"
USUARIOS = "data/users.json"
TWEETS = "data/tweets.json"

if "-v" in sys.argv:
    print ("Twitter Arles 0.1")
    sys.exit(0)

if not os.path.exists ("data/"):
    os.mkdir ("data/")

print("Bienvenido a esta aplicacion.")
login = input("Cuel es tu usuario?")
usuarios ={}


usuarios = cargarFichero(USUARIOS)
    

    



if os.path.exists (USUARIOS):
    fusuarios = open (USUARIOS,"r")
    usuarios = json.load(fusuarios)
    fusuarios.close()

if login not in usuarios.keys():
    print ("Tu usuario no existe, vamos a crearlo")
    nombre = input("Cual es tu nombre? ")
    usuarios[login] = {"id":len(usuarios)+1,"nombre":nombre}
    print (type(usuarios))
    fusuarios = open (USUARIOS,"w")
    json.dump(usuarios,fusuarios)
    fusuarios.close

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
        seguir ={}
        
        if os.path.exists(SEGUIDORES):
            seguir = {}
            fseguir = open(SEGUIDORES, "r")
            
            seguir = json.load(fseguir)
            fseguir.close()
            
            if login in seguir:
                lseguidos = []
                seguidos = seguir[login]
                for usuario,valores in usuarios.items():
                    if valores["id"] in seguidos:
                        
                        lseguidos.append(usuario)
                if os.path.exists(TWEETS):
                    ftweets= open (TWEETS,"r")
                    tweets= json.load(ftweets)
                    ftweets.close();
                    
                    for tweet in tweets:
                        if tweet["Autor"] in lseguidos:
                            print ("Autor: {} Texto: {}".format(tweet["Autor"], tweet["Mensaje"]))
                    
            else:
                print ("No sigues a nadie! Empieza ya mismo a seguir a alguien")    
        
        
        else:
            print ("No sigues a nadie! Empieza ya mismo a seguir a alguien")


    
    
    elif opcion == "2":
        tweets=[]
        if os.path.exists(TWEETS):
            ftweets= open(TWEETS,"r")
            tweets = json.load(ftweets)
            ftweets.close()
        infotweet = pedirtweet(login)
        tweets.append(infotweet)
        ftweets = open(TWEETS,"w")
        print(type(tweets))
        json.dump(tweets,ftweets)
        ftweets.close()
    elif opcion == "3":
        idusuarios=[]
        fusuarios=open(USUARIOS, "r")
        usuarios= json.load(fusuarios)
        fusuarios.close();
        print("Lista de usuarios")
        for usuario in usuarios:
            if usuario != login:
                print ("Id: {} Login: {} Nombre: {}".format(usuarios[usuario]["id"],usuario,usuarios[usuario]["nombre"]))
                idusuarios.append (usuarios[usuario]["id"])
        follow = int(input ("Indica el id (numerico= del usuarios a seguir: "))

        
        if follow in idusuarios:
            seguir ={}
            if os.path.exists(SEGUIDORES):
                fseguir= open(SEGUIDORES,"r")
                seguir = json.load(fseguir)
                fseguir.close()
            if login not in seguir:
                seguir[login]=[]
            seguir[login].append(follow)
            fseguir=open(SEGUIDORES,"w")
            json.dump(seguir,fseguir)
            fseguir.close()
                



    
    
    elif opcion == "4":
        if os.path.exists(TWEETS):
            ftweets = open (TWEETS,"r")
            tweets= json.load(ftweets)
            ftweets.close()
            print("Lista de tus tweets")
            for tweet in tweets:
                if tweet["Autor"]== login:
                    print ("Likes: {} Retwitts: {}\n{}".format(tweet["Likes"],tweet["Retweets"],tweet["Mensaje"]))
        else:
            print("No hay tweets")

def cargarFichero (patch):
    if  not os.path.exists(fichero): return False
    ficherotemp =  open(fichero, "r")
    return json.load (ficherotemp)    


        

        



        



