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

class Pedido:

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0
        for (prod, cant) in zip(self.__productos, self.__cantidades):
            total = total + prod.calcular_total(cant)
        return total

    def mostrar_pedido(self):
        for (prod, cant) in zip(self.__productos, self.__cantidades):
            print("Producto =>", prod.nombre, "|| Cantidades", cant)


p1 = Producto(1,"pollo", 5)
p2 = Producto(2,"pato", 7)
p3 = Producto(3,"gaviota", 9)


print(p1)
print(p2)
print(p3)


print(p1.calcular_total(10))
print(p2.calcular_total(10))
print(p3.calcular_total(10))


lista_productos = [p1,p2,p3]
lista_cantidades = [90,26,3]

pedido = Pedido(lista_productos, lista_cantidades)
print("Total pedido =", str(pedido.total_pedido()))
pedido.mostrar_pedido()