from twitter.tweets.pedir import pedirtweet
fichero = open ("twitter.txt", "a")
fecha = "2018-09-10"
usuario = input ("Nombre de Usuario: ")
infotweet = pedirtweet(usuario)
print (str(infotweet["Retweets"]))

fichero.write(":".join([usuario, infotweet["Mensaje"], fecha, str(infotweet["Likes"]), str(infotweet["Retweets"])])+"\n")
fichero.close()
