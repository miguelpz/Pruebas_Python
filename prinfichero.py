

with open("twitter.txt") as fichero:
    for linea in fichero:
        [usuario,mensaje,fecha,likes,retweets] = linea.split(":")
        print ("*" * 80)
        print ("Autor: {}\nMensaje: {}\nFecha: {}\nLikes: {} Retweets: {}".format(usuario,mensaje,fecha,likes,retweets))

        
