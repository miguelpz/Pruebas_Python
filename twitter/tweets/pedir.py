def pedirtweet(usuario):
    tweet = None
    tweet = input ("Que esta pasando? ")
    likes = int(input("Cuantos likes? "))
    retweets = int(input("Cuantos retweets? "))
    infotweet ={"Autor":usuario, "Mensaje":tweet, "Likes":likes, "Retweets":retweets}
    return infotweet