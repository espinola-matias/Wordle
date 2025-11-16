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