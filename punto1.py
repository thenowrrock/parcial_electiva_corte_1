# Electiva de programación
from collections import Counter
# Enunciado:
#   Cree un diccionario que represente para cada elemento de la siguiente lista, su número de ocurrencias :
#   [‘A’,’a’,’m’,’n’,’o’,’n’,’Z’,’z’,’A’,’p’,’q’,’n’,’u’]

#Mi lista de letras
#letras = ['A', 'a', 'm', 'n', 'o', 'n', 'Z', 'z', 'A', 'p', 'q', 'n', 'u']
letras = ["hola como estas hoy"]


def n_ocurrencias(frase):
    contador = Counter(frase)
    print(contador)
    print(len([t[1] for t in list(contador.items()) if t[1] > 1]))




# solución
#Creamos un diccionario en el cual podemos ir contando mientras vamos leyendo
#Esto hace que se aun poco mas rapido,  i es la variable que recorre la lista, cada vez que vayamos pasando
#Por un elemenot de la lista que se vaya contando con el metodo count(i)
#cuadno nos las este contando que tambien no las asigne de nuevo pero en forma de diccionario {a : 3}

dict = {i:letras.count(i) for i in set(letras)}

#Nos imprima el diccionario con las letras
print(dict)

# Respuesta con modulo de python
#nos cuenta las ocurrencias cada que encuentra elementos semejantes
print(Counter(letras))
print("Numero de ocurrencias de una cadena:")
s = "hola como estas hoy"
n_ocurrencias(s)

