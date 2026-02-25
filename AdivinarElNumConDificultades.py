import random
MINIMO = 1
dificultad = input(f"Selecciona la dificultad : (Facil , Normal , Dificil): ")
if dificultad == "Facil" :
    maximo = 10
elif dificultad ==  "Normal":
    maximo = 20
elif dificultad ==  "Dificil":
    maximo = 30        
elif dificultad not in "facil" or "Facil" or "Normal" or "Dificil" :
    print("Error dificultad erronea, se seleccionara la dificultad facil")
    maximo = 10

numero_azar = random.randint(MINIMO , maximo)
intentos = 0
while True:
    intento_Usuario = int(input(f"escribe un numero [{MINIMO} - {maximo}]"))
    intentos += 1
    if intento_Usuario > numero_azar :
        print("el numero es mas pequeño que " + str (intento_Usuario))
    elif intento_Usuario < numero_azar :
        print("el numero es mas grande que " + str (intento_Usuario))
    else:
  
        break
print ("felicidades atinaste al numero, el numero era: "+ str(numero_azar))        
print(f"solo te tomo, {intentos} intentos.")