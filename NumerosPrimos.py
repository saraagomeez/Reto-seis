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