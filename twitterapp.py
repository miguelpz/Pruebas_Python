creditos = ("Miguel Angel","sutia",2018)
infotweet={}
listatweet=[]
print("Bienvenido a esta aplicacion.")
usuario = input("Cuel es tu nombre?")
otro="s"
i=1

def pedirtweet():
    tweet = None
    tweet = input ("Que esta pasando? ")
    likes = int(input("Cuantos likes? "))
    retweets = int(input("Cuantos retweets? "))
    infotweet ={"Autor":usuario, "Mensaje":tweet, "Likes":likes, "Retweets":retweets}
    return infotweet

def flistatweets (listatweet):
    for tweet in listatweet:
        print(str(tweet))
        likes = tweet['Likes']
        retweets = tweet['Retweets']

        if likes > 2:
            print("Su tweet tiene 'me gustas'")
        elif likes == 1:
            print("Su tweet tiene un me gusta")
        elif likes == 2:
            print("Su tweet tiene dos me gusta")
        else:
            print("Su tweet no tiene 'me gustas'")
        
        if (retweets > 0): print("Este tweet tiene retweets")
    
while (otro == "s"):
    print ("Tweet numero: ", i)
    i += 1
    infotweet = pedirtweet()
    listatweet.append(infotweet)
    otro = input("Desea introducir un nuevo tweet? s/n: ")
    flistatweets (listatweet)
        
        



