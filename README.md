# Adivinar-El-Numero
pequeño juego hecho en python, donde debes adivinar el numero que esta "pensando" la pc en ese momento

el "juego" se divido en dos programas

"AdivinaElNumero" y "AdivinaElNumConDificultades"
en el primer programa "AdivinaElNumero", las reglas son simples.
  -la computadora "piensa" un numero y el usuario debe adivinar, los numero en esta version van del 1 al 10.


en el segundo programa "AdivinaElNumConDificultades"
  es casi lo mismo, solo que el usuario primero debe escribir la dicicultad del juego y con eso los valores posibles cambian.
  - dificultad Facil, la maquina solo "piensa" un valor entre el 1 al 10
  - dificultad Normal, la maquina solo "piensa" en un valor que se encuentre el 1 al 20.
  - Dificultad Dificil, la maquina solo "piensa" un valor que se encuentra entre 1 y 30.
  - en caso de escribir una dificultad invalidad, se ajustara la dificultad en Facil de forma automatica

Caracteristicas.
- Cuenta con un contador que guarda cada intento hasta que el usuario "gana" el juego y muestra en pantalla cuantos intentos tomo.
- El "juego" es interactivo por que el usuario es quien escribe los numero en cada intento.
- ambos "juegos" comparten las caracteristicas de al terminar una partida, indica cuantos intentos tomo.
- Siempre que el usuario introduzca un numero y no sea el que la maquina "penso", aparece un mensaje indicando si el numero que la maquina tiene en "mente" es mayor o menor que el numero ingresado.
