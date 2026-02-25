import random
MINIMO = 1
MAXIMO = 10

numero_azar = random.randint(MINIMO , MAXIMO)
intentos = 0
while True:
    intento_Usuario = int(input(f"escribe un numero [{MINIMO} - {MAXIMO}]: "))
    intentos += 1
    if intento_Usuario > numero_azar :
        print("el numero es mas pequeño que " + str (intento_Usuario))
    elif intento_Usuario < numero_azar :
        print("el numero es mas grande que " + str (intento_Usuario))
    else:
  
        break
print ("felicidades atinaste al numero, el numero era: "+ str(numero_azar))        
print(f"solo te tomo, {intentos} intentos.")