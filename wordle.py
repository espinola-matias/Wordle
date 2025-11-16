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
