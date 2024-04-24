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