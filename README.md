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

```
