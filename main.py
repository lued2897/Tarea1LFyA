#importamos la biblioteca para el uso de expresiones regulares
import re

def testRE(numEj,infile):
    print("Probando ejercicio "+str(numEj+1)+":\n")
    re = ejercicios[numEj]
    file = open(infile, 'r')
    Lines = file.readlines()
    count = 0
    mismatches = 0
    for line in Lines:
        line = line.replace("\n", "")
        columns = line.split(":")
        if(int(columns[0])==numEj+1): #el número de ejercicio coincide con el número de a cadena de entrada
            count += 1
            output = re.fullmatch(columns[1]) #verificamos que la cadena de prueba hace match con la ER correspondiente
            mensaje = "correcto"
            if output and columns[2]=="nm":
                print("\t Error: Según el archivo "+str(infile)+", la cadena '{}' no debería coincidir con la ER '{}'".format(columns[1].strip(),re.pattern)+", pero coincide")   
                mismatches+=1
            elif not output and columns[2]=="m":
                print("\t Error: Según el archivo "+str(infile)+", la cadena '{}' debería coincidir con la ER '{}'".format(columns[1].strip(),re.pattern)+", pero no coincide")
                mismatches+=1
            elif output and columns[2]=="m":
                print("\t Acierto: la cadena '{}' coincide con la ER '{}' como se esperaba".format(columns[1].strip(),re.pattern))    
            elif not output and columns[2]=="nm":
                print("\t Acierto: la cadena '{}' no coincide con la ER '{}' como se esperaba".format(columns[1].strip(),re.pattern))    
    
    if(count==0):
        print("ALERTA:No hay cadenas de prueba para el ejercicio "+str(numEj+1))
    elif(count<10):
        print("\nALERTA: No hay suficientes cadenas de prueba para el ejercicio "+str(numEj+1)+", se sugiere probar con al menos 5 cadenas en el lenguaje y 5 cadenas que no pertenecen al lenguaje.")    
    elif(mismatches!=0):
        print("\nALERTA: La solución para el ejercicio "+str(numEj+1)+" no parece no ser la respuesta correcta, ya que no pasó " +str(mismatches)+ " de las pruebas")
    else:
        print("\nEjercicio "+str(numEj+1)+": CORRECTO (La solución parece ser la respuesta correcta, ya que pasó todas las pruebas)")

            
for n in range(1):
    with open("expresiones.py") as f:
        exec(f.read())
        print("Integrantes del quipo:")
        for i in integrantes:
            print(i)
        print("----------")  
        for ejn in range(7):
            testRE(ejn,"cadenas.txt")
            print("")
    