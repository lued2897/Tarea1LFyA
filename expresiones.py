#importamos la biblioteca para el uso de expresiones regulares
import re

#Sustituir los elementos del arreglo integrantes con los nombres de los integrantes del equipo, nombre seguido de apellidos
integrantes = ["Integrante1","Integrante2","Integrante3"]

#cada elemento del arreglo ejercicios deberá ser la solución al ejercicio correspondiente, es decir ejercicio[n-1] es la solución al ejercicio n
ejercicios = [None]*7

#ejercicio1
ejercicios[0] = re.compile('^[0-9]([5-9][0-9])*$')
#ejercicio2
ejercicios[1] = re.compile('^(?:[13579][0-9])*[13579]?$') # grupo no capturante para guardar memoria al usar (opcional)
#ejercicio
ejercicios[2] = re.compile('[a-z]+')
#ejercicio4
ejercicios[3] = re.compile('[a-z]+')
#ejercicio5
ejercicios[4] = re.compile('[a-z]+')
#ejercicio6
ejercicios[5] = re.compile('[a-z]+')
#ejercicio7
ejercicios[6] = re.compile('[a-z]+')


#para obtener las coincidencias: re.match(string), regresa un arreglo con las coincidencias