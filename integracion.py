import random

# Imprime un mensaje de bienvenida al jugador.
print("Bienvenido a 'Binario vs Decimal'")

# Establece la variable para controlar si el jugador quiere seguir jugando.
jugar_nuevamente = "s"

# Bucle principal del juego que continúa mientras el jugador ingrese 's' (sí).
while jugar_nuevamente.lower() == "s":

    # Muestra las opciones del menú principal.
    print("\n¿Qué querés hacer?")
    print("1. Convertí un número entre sistemas")
    print("2. Adiviná el número binario a partir de un decimal")
    
    # Valida la entrada del modo de juego.
    modo_valido = False
    while modo_valido == False:
        modo = input("Seleccioná una opción (1 o 2): ")
        
        # Verifica si la entrada es '1' o '2'.
        if modo == "1" or modo == "2":
            modo_valido = True
        else:
            # Muestra un mensaje de error si la opción no es válida.
            print("❌ Opción no válida. Elegí 1 o 2.")

    # Si el jugador elige la opción 1 (Convertir entre sistemas).
    if modo == "1":
        print("\n¿Qué tipo de número quiere convertir?")
        print("1. Sistema decimal.")
        print("2. Sistema binario.")
        print("3. Sistema octal.")

        modo_valido = False
        while modo_valido == False:
            modo = input("Seleccioná una opción (1 - 2 - 3: ")
            if modo == "1" or modo == "2" or modo == "3":
                modo_valido = True
            else:
                print("❌ Opción no válida. Elegí 1 o 2 o 3.")

        if modo == "1": # Usuario elige ingresar un número del sistema decimal, ingresa a condicional para elegir a qué sistema convertir su número
            numeroUsuario = int(input("Ingrese el número a convertir: "))
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema binario.")
            print("2. Sistema octal.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")

            if modo == "1": # Conversión de número decimal a binario
                numeroDecABin = numeroUsuario # Creamos una nueva variable con el mismo valor que el número que ingresó el usuario
                binario = 0 # Se inicializa variable binario en 0
                i = 0 # Se inicializa variable i en 0

                # Ciclo para convertir el número decimal a binario
                while numeroDecABin > 0: 
                    # Dividimos el número decimal en 2 con % para obtener resto y lo guardamos en la variable resto
                    resto = numeroDecABin % 2 
                    # Divimos por 2 el número del usuario con // para obtener la parte entera y la guardamos en la misma variable que ingresó el usuario
                    numeroDecABin = numeroDecABin // 2 
                    # Con cada repetición del ciclo acá hacemos el número binario. Multiplicamos el resto por (10 elevado al valor de i) y esto lo sumamos a binario
                    binario += resto * (10**i) 
                    # Sumamos 1 a i
                    i+=1 
                print(f"El número decimal {numeroUsuario} en binario es {binario}.")
            
            # Conversión de número decimal a octal
            elif modo == "2": 
                octal = 0
                i = 0
                numeroDecAOct = numeroUsuario
                while numeroDecAOct > 0:
                    resto = numeroDecAOct % 8
                    octal = resto * (10**i) + octal
                    numeroDecAOct = numeroDecAOct // 8
                    i+=1
                print(f"El número en decimal {numeroUsuario} en octal es {octal}.")

        # Usuario elige ingresar un número del sistema binario, ingresa a condicional para elegir a qué sistema convertir su número
        elif modo == "2": 
            numeroUsuario = input("Ingrese el número a convertir: ")
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema decimal.")
            print("2. Sistema octal.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")
                    
            # Conversión de número binario a decimal
            if modo == "1": 
                numeroBinADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroBinADec % 10
                    decimal = decimal + digito*(2**i)
                    i +=1
                    numeroBinADec = numeroBinADec // 10
                print(f"El número binario {numeroUsuario} en decimal es {decimal}.")
            
            # Conversión de número binario a octal
            elif modo == "2": 
                numeroBinAOct = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroBinAOct % 10
                    decimal = decimal + digito*(2**i)
                    i +=1
                    numeroBinAOct = numeroBinAOct // 10
                octal = 0
                i = 0
                numeroDecAOct = decimal
                while numeroDecAOct > 0:
                    resto = numeroDecAOct % 8
                    octal = resto * (10**i) + octal
                    numeroDecAOct = numeroDecAOct // 8
                    i+=1
                print(f"El número binario {numeroUsuario} en octal es {octal}.")
        
        # Usuario elige ingresar un número del sistema octal, ingresa a condicional para elegir a qué sistema convertir su número
        elif modo == "3": 
            numeroUsuario = input("Ingrese el número a convertir: ")
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema decimal.")
            print("2. Sistema binario.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")

            # Conversión de octal a decimal
            if modo == "1": 
                numeroOctADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroOctADec % 10
                    decimal = decimal + digito*(8**i)
                    i +=1
                    numeroOctADec = numeroOctADec // 10
                print(f"El número octal {numeroUsuario} en decimal es {decimal}.")
            
            # Conversion de octal a binario
            if modo == "2": 
                numeroOctADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroOctADec % 10
                    decimal = decimal + digito*(8**i)
                    i +=1
                    numeroOctADec = numeroOctADec // 10
                #numeroDecABin = decimal # Creamos una nueva variable con el mismo valor que el número que ingresó el usuario
                binario = 0
                i = 0
                while decimal > 0: 
                    resto = decimal % 2
                    decimal = decimal // 2
                    binario += resto * (10**i)
                    i+=1
                print(f"El número octal {numeroUsuario} en binario es {binario}.")

    # Si el jugador elige la opción 2 (Adivinar el número binario).    
    elif modo == "2":
        print("\nADIVINÁ EL BINARIO A PARTIR DE UN DECIMAL")
        print("Elegí un nivel de dificultad:")
        # Se genera un numero comprendido entre 0 y 15
        print("1. Fácil (4 bits)")
        # Se genera un numero comprendido entre 0 y 255        
        print("2. Medio (8 bits)")

        # Valida la entrada de la dificultad.
        dificultad_valida = False
        while dificultad_valida == False:
            opcion = input("Seleccioná una opción (1 o 2): ")
            # Si elige la opción fácil (4 bits).
            if opcion == "1":
                bits = 4
                dificultad_valida = True
            # Si elige la opción media (8 bits).
            elif opcion == "2":
                bits = 8
                dificultad_valida = True
            else:
                # Muestra un mensaje de error si la opción no es válida.
                print("❌ Opción no válida. Elegí 1 o 2.")

        # Calcula el número máximo decimal posible para la cantidad de bits seleccionada.
        max_numero = 2**bits - 1

        # Genera un número decimal aleatorio dentro del rango.
        numero_decimal = random.randint(0, max_numero)
        
        # Convierte el número decimal generado a su representación binaria.
        n = numero_decimal
        numero_binario = ""
        
        # Mientras el número decimal (n) sea mayor que cero (Este bucle extrae los bits de derecha a izquierda)
        while n > 0:
            numero_binario = str(n % 2) + numero_binario
            n = n // 2
        
        # Asegura que el número binario tenga la cantidad de bits correcta, rellenando con ceros a la izquierda si es necesario.
        if numero_binario:  # Si la cadena no está vacía
            numero_binario = numero_binario.zfill(bits)
        else:  # Si es una cadena vacía (caso cuando n=0)
            numero_binario = "0".zfill(bits)   

        # Muestra el número binario correcto (para que el jugador sepa después).
        #print(f"Binario: {numero_binario}")
                
        # Pide al jugador que adivine el número binario correspondiente al decimal mostrado.
        print(f"\nAdiviná el número binario del decimal: {numero_decimal}")
        intento = input("Tu respuesta (binario): ")

        # Valida que la entrada del jugador solo contenga 0s y 1s.
        solo_0_y_1 = True
        for caracter in intento:
            if caracter != "0" and caracter != "1":
                solo_0_y_1 = False
                
        # Verifica si la entrada es válida (solo 0s y 1s y no está vacía).
        if solo_0_y_1 and intento != "":
            # Asegura que la respuesta del jugador tenga la misma cantidad de bits que el número binario correcto.
            intento_usuario = intento.zfill(bits)
            # Compara la respuesta del jugador con el número binario correcto.
            if intento_usuario == numero_binario:
                print("✅ ¡Correcto!")
            else:
                # Si la respuesta es incorrecta, muestra el valor correcto y explica cómo convertir de decimal a binario.
                print(f"❌ Incorrecto. El valor correcto era: {numero_binario}")
                print("\n¿Cómo se convierte un número decimal a binario?")
                print(f" Empezamos dividiendo {numero_decimal} sucesivamente por 2 y guardamos los restos.")

                # Muestra los pasos de la conversión de decimal a binario.
                temp = numero_decimal
                # Se inicializa una lista vacía llamada 'pasos' para almacenar cada paso de la división.
                pasos = []

                while temp > 0:
                    # Mientras el valor temporal sea mayor que 0, se realizan las divisiones sucesivas por 2.
                    cociente = temp // 2
                    resto = temp % 2
                    # Se agrega una cadena formateada a la lista 'pasos' que muestra la división, el cociente y el resto obtenidos.
                    pasos.append(f"  {temp} ÷ 2 = {cociente}, resto = {resto}")
                    temp = cociente

                # Se itera a través de la lista 'pasos' para mostrar cada paso de la conversión al jugador.
                for paso in pasos:
                    print(paso)
                    
                # Se indica al jugador que el número binario se obtiene leyendo los restos de las divisiones de abajo hacia arriba.
                print(f"\n  El resultado en binario (leyendo los restos de abajo hacia arriba) es: {numero_binario}")
        else:
            # Si la entrada no es válida, muestra un mensaje de error y el valor correcto.
            print("❌ Entrada inválida. Solo se permiten 0 y 1.")
            print(f"El valor correcto era: {numero_binario}")

    # Pregunta al jugador si quiere volver al menú principal.
    jugar_nuevamente = input("\n¿Querés volver al menú principal? (s/n): ")

# Mensaje de agradecimiento al finalizar el juego.
print("¡Gracias por usar Binario vs Decimal!")
