import random

print("Bienvenido a 'Binario vs Decimal'")
intentos = 0
jugar_nuevamente = "s"

while jugar_nuevamente.lower() == "s":

    print("\n¿Qué querés hacer?")
    print("1. Convertí un número entre sistemas")
    print("2. Adiviná el número binario a partir de un decimal")

    modo_valido = False
    while modo_valido == False:
        modo = input("Seleccioná una opción (1 o 2): ")
        if modo == "1" or modo == "2":
            modo_valido = True
        else:
            print("❌ Opción no válida. Elegí 1 o 2.")

    if modo == "1":
        pass
        
    elif modo == "2":
        print("\nADIVINÁ EL BINARIO A PARTIR DE UN DECIMAL")
        print("Elegí un nivel de dificultad:")
        print("1. Fácil (4 bits)")
        print("2. Medio (8 bits)")

        dificultad_valida = False
        while dificultad_valida == False:
            opcion = input("Seleccioná una opción (1 o 2): ")
            if opcion == "1":
                bits = 4
                dificultad_valida = True
            elif opcion == "2":
                bits = 8
                dificultad_valida = True
            else:
                print("❌ Opción no válida. Elegí 1 o 2.")

        max_numero = 2**bits - 1
        numero_decimal = random.randint(0, max_numero)
        numero_binario = bin(numero_decimal)[2:].zfill(bits)

        print(f"\nAdiviná el número binario del decimal: {numero_decimal}")
        intento = input("Tu respuesta (binario): ")

        solo_0_y_1 = True
        for caracter in intento:
            if caracter != "0" and caracter != "1":
                solo_0_y_1 = False

        if solo_0_y_1 and intento != "":
            intento_usuario = intento.zfill(bits)
            if intento_usuario == numero_binario:
                print("✅ ¡Correcto!")
            else:
                print(f"❌ Incorrecto. El valor correcto era: {numero_binario}")
                print("\n¿Cómo se convierte un número decimal a binario?")
                print(f"  Empezamos dividiendo {numero_decimal} sucesivamente por 2 y guardamos los restos.")

                temp = numero_decimal
                pasos = []

                while temp > 0:
                    cociente = temp // 2
                    resto = temp % 2
                    pasos.append(f"  {temp} ÷ 2 = {cociente}, resto = {resto}")
                    temp = cociente

                for paso in pasos:
                    print(paso)

                print(f"\n  El resultado en binario (leyendo los restos de abajo hacia arriba) es: {numero_binario}")
        else:
            print("❌ Entrada inválida. Solo se permiten 0 y 1.")
            print(f"El valor correcto era: {numero_binario}")

    jugar_nuevamente = input("\n¿Querés volver al menú principal? (s/n): ")

print("¡Gracias por usar Binario vs Decimal!")
