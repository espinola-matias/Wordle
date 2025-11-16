def definir_parametros():
    max_letras = 10
    min_intentos = 3
    max_intentos = 20
    intentos_maximos = 0
    
    print("¡BIENVENIDO AL DESAFIO WORDLE!")
    print("¡ELIGE LA PALABRA QUE DEBERA ADIVINAR EL ADVERSARIO!\n")
    while True:
        palabra_encontrar = input(f"Dime la palabra que quieres ocultar (max {max_letras} letras): ").lower()
        
        if not palabra_encontrar.isalpha() or not palabra_encontrar:
            print("¡ALERTA!: La palabra solo debe contener letras del abecedario y no puede estar vacia")
            continue 
        
        if len(palabra_encontrar) > max_letras:
            print(f"¡ALERTA!: La palabra es demasiado larga. No debe superar las {max_letras} letras")
            continue
            
        cantidad_letras = len(palabra_encontrar)
        print(f"\nPalabra oculta establecida: {palabra_encontrar.upper()}. Largo: {cantidad_letras} letras")
        break

    while intentos_maximos == 0:
        try:
            cantidad_intentos = int(input(f"¿Cuantos intentos deseas dar? (Minimo {min_intentos}, Maximo {max_intentos}): "))

            if cantidad_intentos < min_intentos:
                intentos_maximos = min_intentos
                print(f"¡Demasiado dificil! Se inicializa el minimo de *{min_intentos}* intentos")
            
            elif cantidad_intentos > max_intentos:
                intentos_maximos = max_intentos
                print(f"¡Demasiado facil! Se inicializa el maximo de *{max_intentos}* intentos")
            
            else:
                intentos_maximos = cantidad_intentos
                
        except ValueError:
            print("¡ALERTA!: Por favor, introduce un numero entero valido para los intentos")
            continue 
            
    print(f"Tienes *{intentos_maximos}* oportunidades para adivinar la palabra")
    
    return palabra_encontrar, intentos_maximos, cantidad_letras

def obtener_pista():
    pista = "" 
    while True:
        try:
            respuesta = int(input("\n¿Deseas dejar una pista para el jugador? (1: Si, dejar pista | 2: No, dejar el juego dificil): "))

            if respuesta == 1:
                pista = input("Escribe tu pista (ej: 'Es sobre fútbol', 'Palabra en ingles'): ")
                if not pista:
                     pista = "El creador dejo el espacio vacio, ¡pero al menos elegiste dejar una pista!"
                break
            
            elif respuesta == 2:
                print("\n¡Maxima dificultad seleccionada!")
                pista = "¡Esta dificil! El creador no dejo ninguna pista ¡Adivina a ciegas!"
                break
                
            else:
                print("Opción no valida. Por favor, ingresa solo '1' o '2'")
                continue

        except ValueError:
            print("¡ALERTA!: Por favor, introduce un numero entero (1 o 2)")
            continue
            
    return pista

def verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada):
    resultado = []
    cantidad_de_letras = len(palabra_a_encontrar) 

    for posicion in range(cantidad_de_letras):
        letra_ingresada = palabra_ingresada[posicion]
        
        las_letras_son_iguales = palabra_a_encontrar[posicion] == letra_ingresada
        la_letra_existe = letra_ingresada in palabra_a_encontrar

        if las_letras_son_iguales:
            resultado.append('[' + letra_ingresada.upper() + ']')
        elif la_letra_existe:
            resultado.append('(' + letra_ingresada.lower() + ')')
        else: 
            resultado.append(letra_ingresada.lower())

    return resultado

def imprimir_grilla(grilla):
    print("\n--- RESPUESTA ACTUAL ---")
    for fila in grilla:
        print(" ".join(fila))
    print("--------------------\n")

def jugar():
    
    palabra_a_encontrar, intentos_restantes, cantidad_de_letras = definir_parametros()
    pista_jugador = obtener_pista() 
    grilla = [] 

    print("\n" + "="*50)
    print("¡BIENVENIDO AL DESAFIO WORDLE!")
    print("="*50)
    print(f"El desafio es adivinar una palabra de *{cantidad_de_letras}* letras. Y tienes {intentos_restantes} intentos")
    print("\n**COMO INTERPRETAR LOS RESULTADOS:**")
    print(f"  - **[A]** (Corchetes): La letra 'A' esta en la palabra y esta en la **POSICION CORRECTA**")
    print(f"  - **(B)** (Paréntesis): La letra 'B' esta en la palabra, pero en la **POSICIoN INCORRECTA**")
    print(f"  - **c** (Minuscula simple): La letra 'c' **NO EXISTE** en la palabra secreta")
    
    print(f"\n**PISTA DEL CREADOR:** {pista_jugador}")
    print("\n" + "="*50) 

    while intentos_restantes > 0:        
        print(f"\n¡Te quedan {intentos_restantes} intentos!")
        
        palabra_ingresada = input(f"Adivina la palabra ({cantidad_de_letras} letras): ").lower()
        if len(palabra_ingresada) != cantidad_de_letras:
            print(f"¡Ojo! Ingrese una palabra con *{cantidad_de_letras}* letras exactas. Intentelo de nuevo")
            continue 
            
        if not palabra_ingresada.isalpha():
             print("¡Solo se permiten letras del abecedario! Sin numeros, ni simbolos")
             continue
        
        linea_verificada = verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada)
        
        grilla.append(linea_verificada)
        intentos_restantes -= 1
        
        imprimir_grilla(grilla)

        if palabra_ingresada == palabra_a_encontrar:
            print("¡FELICIDADES, GANASTE! Eres un maestro de las palabras")
            break

    if intentos_restantes == 0 and palabra_ingresada != palabra_a_encontrar:
        print("¡Se te acabaron los intentos!")
        print(f"La palabra secreta era: **{palabra_a_encontrar.upper()}**")

if __name__ == "__main__":
    jugar()