# Electiva de programación
from collections import Counter


################################################################
#Pruebas
listas = ["Ak-47","M16","Mt22.s1","alrmWsx_z"]
lista2 = ["Calibre:7,56","Calibre:5.56","Calibre:882md","Calibre:otrers22"]

tuple = {i:listas.count(i) for i in set(listas)}
def caracteres_comunes(tupla):
        lista1 = ["Ak-47", "M16", "Mt22.s1", "alrmWsx_z"]
        lista2 = ["Calibre:7,56", "Calibre:5.56", "Calibre:882md", "Calibre:otrers22"]

        contador1 = Counter(lista1)
        contador2 = Counter(lista2)

        comunes = contador1 & contador2

        if(comunes) == 0:
            return None

        comunes = list(comunes.elements())
        comunes = sorted(comunes)

        print(comunes)
        return comunes

################################################################
#Pruebas
def caracteres_comunes2(cad1,cad2):
        cont1 = Counter(cad1)
        cont2 = Counter(cad2)

        comunes = cont2 & cont1
        comunes = list(comunes.elements())
        comunes = sorted(comunes)

        print(comunes)
        return comunes


################################################################

def funcion():
        #Entrada
        listInput = ["decir", "balneario", "habria", "cabria", "seria", "abanico", "quesera", "mentir"]
        listOutput = []
        flag = False  #bandera de stop en el sistema


        print("Entrada de lista :")  , print(listInput)
        print("")

        #Calcular ciclo en el cual se realiza la ejecucion del sistema , donde se escoje y verifica la palabra
        while (flag == False):
                #Variables Aux
                xAux = -1
                yAux = -1
                c = 0
                r = 0
                repitenAux = 0
                if (len(listInput) != 0):
                        for x in listInput:
                                xAux = xAux + 1
                                for y in listInput:
                                        yAux = yAux + 1
                                        if (x != y):
                                                for z in x:
                                                        if (y.count(z) != 0):
                                                                r = r + 1

                                                if (r > repitenAux):
                                                        repitenAux = r
                                                        idx = x
                                                        idy = y

                                                r = 0
                        #Si la palabra esta y se comprobo , se agrega en la tupla , con la mas semejante a ella
                        if (c == 0):
                                tupla = (idx, idy)
                                listInput.remove(idx)
                                listInput.remove(idy)
                                listOutput.append(tupla)
                                c = 1

        #Salida
                elif (len(listInput) == 0):
                        flag = True

        print("")
        print("Salida de la  tupla :") , print(listOutput)
        print("")
################################################################


################################################################
#Salida

#lista_de_listas =  listas + lista2
#tuple ={i:lista_de_listas.count(i) for i in set(lista_de_listas)}
print("**************************************")
print("Caracteres Comunes: ")
print(caracteres_comunes(tuple))
print("**************************************")
print(tuple)
print("**************************************")
print(Counter(tuple))
print("**************************************")
print(len(listas))
print("**************************************")
print(len(lista2))
print("**************************************")
print(funcion())
print("**************************************")
################################################################
















