#importamos la biblioteca para el uso de expresiones regulares
import re

#Sustituir los elementos del arreglo integrantes con los nombres de los integrantes del equipo, nombre seguido de apellidos
integrantes = ["Emmanuel Jimenez Cordova","Grecia Irais Meneses Calderas","Luis Eduardo Perez Osorio"]

#cada elemento del arreglo ejercicios deberá ser la solución al ejercicio correspondiente, es decir ejercicio[n-1] es la solución al ejercicio n
ejercicios = [None]*7

#ejercicio1
ejercicios[0] = re.compile('^[0-9]([5-9][0-9])*$')
#ejercicio2
ejercicios[1] = re.compile('^([13579][0-9])*[13579]?$')
#ejercicio
ejercicios[2] = re.compile('((a[ab])|(a[ab]a)|(a[ab]a[ab])|(a[ab]a[ab]a))|((a[ab]a[ab]aa)+(|a|(a[ab])|(a[ab]a)|(a[ab]a[ab])|(a[ab]a[ab]a)))') #'^(?=(?:a[ab])*a?$)(?=(?:[ab]{2}a)*[ab]{0,2}$)[ab]+$'
#ejercicio4
ejercicios[3] = re.compile('^[aeiou]([a-z]{2}|[a-z]*[aeiou][a-z]{2})')
#ejercicio5
ejercicios[4] = re.compile('^(?![a-z]*[aeiou]{3})[a-z]*$') 
#ejercicio6
ejercicios[5] = re.compile('(?=[a-z]*[aiueo])(?=[a-z]*[bcdfghjklmnpqrstvwxyz][a-z]*[bcdfghjklmnpqrstvwxyz][a-z]*)[a-z]*|[bcdfghjklmnpqrstvwxyz]*')
#ejercicio7
ejercicios[6] = re.compile('([13579](\d){2,}[13579]|[02468](\d){2,}[02468])')


#para obtener las coincidencias: re.match(string), regresa un arreglo con las coincidencias