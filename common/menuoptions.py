from twitter.tweets.listar import flistatweets
from twitter.tweets.pedir import pedirtweet
from common.functions import *
from config.config import *

import sys
import os

infotweet={}
listatweet=[]

def mostrarTimeline (login,usuarios):
 
    seguir ={}
    
    

            
    if os.path.exists(SEGUIDORES):
        seguir = {}
        seguir = cargarFichero(SEGUIDORES)
        
        
        if login in seguir:
            lseguidos = []
            seguidos = seguir[login]
            for usuario,valores in usuarios.items():
                if valores["id"] in seguidos:
                    
                    lseguidos.append(usuario)
            if os.path.exists(TWEETS):
                tweets = cargarFichero(TWEETS)
            
                opcion="n"
                
                
            
            otro="s"
            while otro =="s":
                indice = 0
                for tweet in tweets:
                    if tweet["Autor"] in lseguidos:
                        
                        indice +=1
                        tweet["id"] = str(indice)
                        print ("{}     Autor: {} Texto: {} Likes: {} Retweets: {}".format(tweet["id"], tweet["Autor"], tweet["Mensaje"], tweet["Likes"], tweet["Retweets"]))
                    else:
                        
                        tweet["id"]="NoSeguido"
                                                    
                

                opcion = input ("Indique numero para modificar likes/retweets [s] para salir: ")

                
                    
                if opcion!="s":
                
                    likes = input ("Likes? ")
                    retwets = input ("Retweets? ")

                    for tweet in tweets:
                        if tweet["id"] in opcion:
                            tweet["Likes"]=str(likes)
                            tweet["Retweets"]= str(retwets)
                    
                    for tweet in tweets:
                        tweet.pop("id")
                    
                otro= input ("Modificar otro tweet[s/n]? ")

            escribirFichero(TWEETS,tweets)                          
                
            



                            

                
        else:
            print ("No sigues a nadie! Empieza ya mismo a seguir a alguien")    
       
    else:
        print ("No sigues a nadie! Empieza ya mismo a seguir a alguien")

def escribirNuevoTweet(login,usuarios):

    tweets=[]
    if os.path.exists(TWEETS):
        tweets=cargarFichero(TWEETS)
        
    infotweet = pedirtweet(login)
    tweets.append(infotweet)
    escribirFichero(TWEETS,tweets)

def seguirUsuario(login,usuarios):

    idusuarios=[]
    fusuarios=cargarFichero(USUARIOS)
    
    print("Lista de usuarios")
    for usuario in usuarios:
        if usuario != login:
            print ("Id: {} Login: {} Nombre: {}".format(usuarios[usuario]["id"],usuario,usuarios[usuario]["nombre"]))
            idusuarios.append (usuarios[usuario]["id"])
    follow = int(input ("Indica el id (numerico= del usuarios a seguir: "))

    
    if follow in idusuarios:
        seguir ={}
        if os.path.exists(SEGUIDORES):
            seguir=cargarFichero(SEGUIDORES)
            
        if login not in seguir:
            seguir[login]=[]
        seguir[login].append(follow)
        
        escribirFichero(SEGUIDORES,seguir)

def mostrarMisTweets (login,usuarios):
    if os.path.exists(TWEETS):
        tweets=cargarFichero(TWEETS)
        
        print("Lista de tus tweets")
        
    for tweet in tweets:
        if tweet["Autor"]== login:
            print ("Likes: {} Retwitts: {}\n{}".format(tweet["Likes"],tweet["Retweets"],tweet["Mensaje"]))
    else:
        print("No hay tweets")       