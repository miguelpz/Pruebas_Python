import json

def cargarFichero (path):
        ficherotemp =  open(path, "r")    
        resultado = json.load (ficherotemp)
        ficherotemp.close()
        return resultado 


def escribirFichero (path, data):
    fichero = open (path,"w")
    json.dump (data,fichero)
    fichero.close()