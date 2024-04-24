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

**2) Palíndromo**
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

**3) Números primos**
```

```
