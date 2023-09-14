from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return Elemento.nombre == Elemento.nombre


class Conjunto:
    contador: int = 0

    def __init__(self, nombre):
        self.elementos: list[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self._id = Conjunto.contador

    @property
    def __id(self):
        return self._id

    def contiene(self, elemento) -> bool:
        if isinstance(elemento, Elemento):
            for elem in self.elementos:
                if elem.nombre == elemento.nombre:
                    return True
        return False

    def agregar_elemento(self, elemento):
        if isinstance(elemento, Elemento):
            if not self.contiene(elemento):
                self.elementos.append(elemento)
                return True
        return False

    def unir(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            for elemento in otro_conjunto.elementos:
                if not self.contiene(elemento):
                    self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            conjunto_2 = Conjunto(f"{self.nombre}_{otro_conjunto.nombre}")
            conjunto_2.elementos = self.elementos.copy()
            conjunto_2.unir(otro_conjunto)
            return conjunto_2

    @classmethod
    def intersectar(cls, conjunto, otro_conjunto):
        if isinstance(conjunto, Conjunto) and isinstance(otro_conjunto, Conjunto):
            interseccion_elementos = [elem for elem in conjunto.elementos if otro_conjunto.contiene(elem)]
            interseccion_nombre = f"{conjunto.nombre} INTERSECTADO {otro_conjunto.nombre}"
            interseccion_conjunto = Conjunto(interseccion_nombre)
            interseccion_conjunto.elementos = interseccion_elementos
            return interseccion_conjunto

    def __str__(self):
        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


# Creación de elementos y conjuntos
e_1 = Elemento("1")
e_2 = Elemento("1")
e_3 = Elemento("-4")
e_4 = Elemento("6")

c_1 = Conjunto("Números Naturales")
c_1.agregar_elemento(e_1)
c_1.agregar_elemento(e_4)

c_2 = Conjunto("Números Enteros")
c_2.agregar_elemento(e_3)
c_2.agregar_elemento(e_2)

# print de los conjuntos
print(c_1)
print(c_2)

# unir y print
union = c_1 + c_2
print(union)

# Calcular la intersección de c_1 y c_2
interseccion = Conjunto.intersectar(c_1, c_2)
print(interseccion)


