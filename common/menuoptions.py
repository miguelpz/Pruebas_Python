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
            
                
                for tweet in tweets:
                    if tweet["Autor"] in lseguidos:
                        print ("Autor: {} Texto: {}".format(tweet["Autor"], tweet["Mensaje"]))
                
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