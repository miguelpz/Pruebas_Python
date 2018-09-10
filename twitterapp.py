from twitter.tweets.listar import flistatweets
from twitter.tweets.pedir import pedirtweet



creditos = ("Miguel Angel","sutia",2018)
infotweet={}
listatweet=[]
print("Bienvenido a esta aplicacion.")
usuario = input("Cuel es tu nombre?")
otro="s"
i=1

    
while (otro == "s"):
    print ("Tweet numero: ", i)
    i += 1
    infotweet = pedirtweet(usuario)
    listatweet.append(infotweet)
    otro = input("Desea introducir un nuevo tweet? s/n: ")
    flistatweets (listatweet)
        
        



