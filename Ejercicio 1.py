class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, new_codigo):
        self.__codigo = new_codigo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, new_precio):
        self.__precio = new_precio

    def calcular_total(self, cantidad):
        return self.__precio * cantidad
    def __str__(self):
        return "Código: " + str(self.__codigo) + " || Nombre: " + self.__nombre + " || Precio: " + str(self.__precio)

p1 = Producto(1, "pollo", 5)
p2 = Producto(2, "pato", 7)
p3 = Producto(3, "gaviota", 9)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(10))
print(p2.calcular_total(10))
print(p3.calcular_total(10))