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
```
import math
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
    
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y
    

    def compute_distance(self, other_point):
        try:
            distance = ((self._x - other_point.get_x())**2 + (self._y - other_point.get_y())**2)**0.5
            return distance
        except AttributeError:
            print("Error: uno de los puntos no es valido.")
            return None
    
class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def compute_lenght(self):
        try:
            lenght = ((self._end._x - self._start.get_x())**2 + (self._end._y - self._start.get_y())**2)**0.5
            return lenght
        except AttributeError:
            print("Error: uno de los puntos que define la linea no es valido.")
    
class Shape:
    def __init__(self, is_regular: bool):
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []
        self._inner_angles = []

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

class Triangle(Shape):
    def __init__(self, is_regular: bool):
        super().__init__(is_regular)

class Isosceles(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
    
    def compute_area(self):
        try:
            lenght_edgeB = edgeB.compute_lenght()
            lenght_edgeC = edgeC.compute_lenght()
            base = edgeC.compute_lenght()
            height = ((lenght_edgeB)**2 - (lenght_edgeC/2)**2)**0.5
            return (base * height) / 2
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            lenght_edgeA = edgeA.compute_lenght()
            lenght_edgeB = edgeB.compute_lenght()
            lenght_edgeC = edgeC.compute_lenght()
            return lenght_edgeA + lenght_edgeB + lenght_edgeC
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleA + angleB + angleC
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeA = Point(0,0)
verticeB = Point(4,0)
verticeC = Point(2,4)

edgeA = Line(verticeB,verticeC)
edgeB = Line(verticeC, verticeA)
edgeC = Line(verticeA, verticeB)

angleA = 63.4
angleB = 63.4
angleC = 53.1

vertices = [verticeA, verticeB, verticeC]
edges = [edgeA, edgeB, edgeC]
inner_angles = [angleA, angleB, angleC]

isosceles_triangle = Isosceles(False, vertices, edges, inner_angles)
print("Isoceles area: ", isosceles_triangle.compute_area())
print("Isosceles perimeter: ", isosceles_triangle.compute_perimeter())
print("Isosceles inner angles: ", isosceles_triangle.compute_inner_angles())
print("\n")

class Equilateral(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        try:
            lenght_edgeE = edgeE.compute_lenght()
            lenght_edgeF = edgeF.compute_lenght()
            base = edgeF.compute_lenght()
            height = verticeF.compute_distance(point_height)
            return (base * height) / 2
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            lenght_edgeD = edgeD.compute_lenght()
            lenght_edgeE = edgeE.compute_lenght()
            lenght_edgeF = edgeF.compute_lenght()
            return lenght_edgeD + lenght_edgeE + lenght_edgeF
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleD + angleE + angleF
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeD = Point(0,0)
verticeE = Point(6,0)
verticeF= Point(3, 5.1961)
point_height = Point(3,0)

edgeD = Line(verticeE,verticeF)
edgeE = Line(verticeF, verticeD)
edgeF = Line(verticeD, verticeE)

angleD = 60
angleE = 60
angleF = 60

vertices = [verticeD, verticeE, verticeF]
edges = [edgeD, edgeE, edgeF]
inner_angles = [angleD, angleE, angleF]

equilateral_triangle = Equilateral(True, vertices, edges, inner_angles)
print("Equilateral area: ", equilateral_triangle.compute_area())
print("Equilateral perimeter: ", equilateral_triangle.compute_perimeter())
print("Equilateral inner angles: ", equilateral_triangle.compute_inner_angles())
print("\n")

class Scalene(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        try:
            base = edgeI.compute_lenght()
            height = verticeI.compute_distance(point_height)
            return (base * height) / 2
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            lenght_edgeG = edgeG.compute_lenght()
            lenght_edgeH = edgeH.compute_lenght()
            lenght_edgeI = edgeI.compute_lenght()
            return lenght_edgeG + lenght_edgeH + lenght_edgeI
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleG + angleH + angleI
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeG = Point(0,0)
verticeH = Point(9,0)
verticeI= Point(3,5)
point_height = Point(3,0)

edgeG = Line(verticeH,verticeI)
edgeH = Line(verticeI, verticeG)
edgeI = Line(verticeG, verticeH)

angleG = 59.03
angleH = 39.80
angleI = 81.15

vertices = [verticeG, verticeH, verticeI]
edges = [edgeG, edgeH, edgeI]
inner_angles = [angleG, angleH, angleI]

scalene_triangle = Scalene(False, vertices, edges, inner_angles)
print("Scalene area: ", scalene_triangle.compute_area())
print("Scalene perimeter: ", scalene_triangle.compute_perimeter())
print("Scalene inner angles: ", scalene_triangle.compute_inner_angles())
print("\n")

class TriRectangle(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        try:
            base = edgeL.compute_lenght()
            height = edgeK.compute_lenght()
            return (base * height) / 2
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            lenght_edgeJ = edgeJ.compute_lenght()
            lenght_edgeK = edgeK.compute_lenght()
            lenght_edgeL = edgeL.compute_lenght()
            return lenght_edgeJ + lenght_edgeK + lenght_edgeL
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleJ + angleK + angleL
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeJ = Point(0,0)
verticeK = Point(4,0)
verticeL= Point(0,6)

edgeJ = Line(verticeK,verticeL)
edgeK = Line(verticeL, verticeJ)
edgeL = Line(verticeJ, verticeK)

angleJ = 90
angleK = 45
angleL = 45

vertices = [verticeJ, verticeK, verticeL]
edges = [edgeJ, edgeK, edgeL]
inner_angles = [angleJ, angleK, angleL]

tri_rectangle_triangle = TriRectangle(False, vertices, edges, inner_angles)
print("Triangle rectangle area: ", tri_rectangle_triangle.compute_area())
print("Triangle rectangle perimeter: ", tri_rectangle_triangle.compute_perimeter())
print("Triangle rectangle inner angles: ", tri_rectangle_triangle.compute_inner_angles())
print("\n")

class Rectangle(Shape):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        try:
            width = edgeN.compute_lenght() or edgeP.compute_lenght()
            lenght = edgeM.compute_lenght() or edgeO.compute_lenght()
            return width * lenght
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            width = edgeN.compute_lenght() or edgeP.compute_lenght()
            lenght = edgeM.compute_lenght() or edgeO.compute_lenght()
            return (width * 2) + (lenght * 2)
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleM + angleN + angleO + angleP
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeM = Point(0,0)
verticeN = Point(8,0)
verticeO= Point(8,4)
verticeP= Point(0,4)

edgeM = Line(verticeN,verticeO)
edgeN = Line(verticeO, verticeP)
edgeO = Line(verticeP, verticeM)
edgeP = Line(verticeM, verticeN)

angleM = 90
angleN = 90
angleO = 90
angleP = 90

vertices = [verticeM, verticeN, verticeO, verticeP]
edges = [edgeM, edgeN, edgeO, edgeP]
inner_angles = [angleM, angleN, angleO, angleP]

rectangle = Rectangle(False, vertices, edges, inner_angles)
print("Rectangle area: ", rectangle.compute_area())
print("Rectangle perimeter: ", rectangle.compute_perimeter())
print("Rectangle inner angles: ", rectangle.compute_inner_angles())
print("\n")

class Square(Rectangle):
    def __init__(self, is_regular: bool, vertices: list, edges: list, inner_angles: list):
        super().__init__(is_regular, vertices, edges, inner_angles)

    def compute_area(self):
        try:
            side = edgeQ.compute_lenght() or edgeR.compute_lenght() or edgeT.compute_lenght() or edgeU.compute_lenght()
            return side**2
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_perimeter(self):
        try:
            side = edgeQ.compute_lenght() or edgeR.compute_lenght() or edgeT.compute_lenght() or edgeU.compute_lenght()
            return side * 4
        except AttributeError:
            print("Error: asegurese que las aristas esten definidos.")
    
    def compute_inner_angles(self):
        try:
            return angleQ + angleR + angleT + angleU
        except TypeError:
            print("Error: asegurese que los angulos esten definidos.")
    
verticeQ = Point(0,0)
verticeR = Point(5,0)
verticeT= Point(5,5)
verticeU= Point(0,5)

edgeQ = Line(verticeR,verticeT)
edgeR = Line(verticeT, verticeU)
edgeT = Line(verticeU, verticeQ)
edgeU = Line(verticeQ, verticeR)

angleQ = 90
angleR = 90
angleT = 90
angleU = 90

vertices = [verticeQ, verticeR, verticeT, verticeU]
edges = [edgeQ, edgeR, edgeT, edgeU]
inner_angles = [angleQ, angleR, angleT, angleU]

square = Square(True, vertices, edges, inner_angles)
print("Square area: ", square.compute_area())
print("Square perimeter: ", square.compute_perimeter())
print("Square inner angles: ", square.compute_inner_angles())
print("\n")
```
