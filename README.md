# Reto-seis

## Punto uno

**1) Calculadora:**
```
def realizar_operacion(num1, num2, operador):
        try:
            if operador == '+':
                resultado = num1 + num2 
            elif operador == '-':
                resultado = num1 - num2 
            elif operador == '*':
                resultado = num1 * num2 
            elif operador == '/':
                if num2 != 0:
                    resultado = num1 / num2 
                else:
                    raise ZeroDivisionError("Error: division por 0 no es permitida.")
            else:
                return "Operador no valido, por favor ingrese '+', '-', '*' o '/'."
            return resultado
        except ZeroDivisionError:
            print("Error: division por 0 no es permitida.")


if __name__ == "__main__":
    #Para solicitar entrada del usuario.
    try:
        num1 = float(input("Ingrese el primer numero: "))
        operador = input("Ingrese la operacion (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))

        #Para realizar la operación.
        resultado = realizar_operacion(num1, num2, operador)

        #Para imprimir el resultado.
        print("El resultado de", num1, operador, num2, "es:", resultado)
    except ValueError:
        print("Error: entrada de datos invalida.")
```

**2) Palíndromo:**
```
def palindromo(palabra):
    if not palabra.isalpha():
            raise ValueError("La entrada debe ser una cadena de texto.")
    
    longitud = len(palabra)
    inicio = 0
    fin = longitud - 1

    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

try:
    #Requerir entrada del usuario.
    palabra_usuario = input("Ingrese una palabra o una frase sin espacios en minúsculas: ")

    resultado = palindromo(palabra_usuario)

    #Definir si es palíndromo o no.
    if palindromo(palabra_usuario):
        print(palabra_usuario, "si es un palindromo.")
    else:
        print(palabra_usuario, "no es un palindromo.")
except ValueError as error:
     print("Error:", {error})
```

**3) Números primos:**
```
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primos(lista):
    primos = [num for num in lista if primo(num)]
    return primos

try:
    lista_usuario = input("Ingrese una lista de numeros separados por espacios: ")
    numeros = [int(num) for num in lista_usuario.split()]
except ValueError:
    print("Error: los datos deben ser valores numericos.")
    numeros = []

resultado = obtener_primos(numeros)
print("Numeros primos: ", resultado)
```

**4) Suma consecutiva:**
```
def mayor_suma_consecutiva(lista):
    if len(lista) < 2:
        raise ValueError("La lista debe tener al menos dos elementos")
    
    mayor_suma = lista[0] + lista[1]

    for i in range (1, len(lista)-1):
        suma_consecutiva = lista[i] + lista[i + 1]
        if suma_consecutiva > mayor_suma:
            mayor_suma = suma_consecutiva
    return mayor_suma

try:
    numeros_usuario = input("Ingrese una lista de numeros separada por espacio: ")
    numeros = [int(num) for num in numeros_usuario.split()]
except ValueError:
    print("Error: los resultados deben ser valores numericos.")
    numeros = []

try:
    resultado = mayor_suma_consecutiva(numeros)
    print("La mayor suma consecutiva es: ", resultado)
except ValueError as e:
    print("Error:", {e})
```

**5) Mismos carácteres:**
```
def mismos_caracteres(cadena1, cadena2):
    if not cadena1.isalpha():
        raise ValueError("La entrada debe ser una cadena de texto.")
    
    if not cadena2.isalpha():
        raise ValueError("La entrada debe ser una cadena de texto.")
    
    return sorted(cadena1) == sorted(cadena2)

def cadenas_mismos_caracteres(lista):
    resultados = []

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if mismos_caracteres(lista[i], lista[j]):
                resultados.append(lista[i])
                resultados.append(lista[j])
    return resultados

try:
    entrada_usuario = input("Ingrese una lista de cadenas separada por espacio: ")
    cadenas_usuario = entrada_usuario.split()

    salida = cadenas_mismos_caracteres(cadenas_usuario)
    print(salida)
except ValueError as e:
    print("Error:", {e})
```

## Punto dos
