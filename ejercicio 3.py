''' Nuestro escogimos este metodo para facilitar el uso de las operaciones de la tienda,
haciendo que sea más fácil la gestion del inventario. Además, la interfaz sencilla nos 
permite registrar las compras y calcular el total y el vuelto de forma fácil.'''

# Clase para representar un producto
class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}: ${self.precio}, Cantidad en stock: {self.cantidad}"

# Clase para la gestión de la tienda
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad=0):
        # Agrega un nuevo producto o actualiza la cantidad si ya existe
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad += cantidad
                return
        nuevo_producto = Producto(nombre, precio, cantidad)
        self.productos.append(nuevo_producto)

    def vender_producto(self, nombre, cantidad, monto_cliente):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    total_a_pagar = producto.precio * cantidad
                    producto.cantidad -= cantidad
                    vuelto = monto_cliente - total_a_pagar
                    return f"Total a pagar: ${total_a_pagar}, Vuelto: ${vuelto}"
                else:
                    return "Cantidad insuficiente en stock"
        return "Producto no encontrado"

    def recibir_proveedor(self, nombre, cantidad, precio_sugerido):
        self.agregar_producto(nombre, precio_sugerido, cantidad)
        return f"Producto {nombre} recibido de proveedor con {cantidad} unidades y precio sugerido de ${precio_sugerido}."

    def mostrar_inventario(self):
        print("\n--- Inventario Actual ---")
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos:
            print(producto)

# Función para gestionar compras de clientes
def gestionar_compras(tienda):
    print("\n--- Gestión de Compras para Clientes ---")
    tienda.mostrar_inventario()  # Mostrar inventario antes de la compra para que el cliente pueda escoger lo que deseea y tambien muestra los productos en existencia
    nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
    cantidad = int(input(f"Ingrese la cantidad que desea comprar de {nombre_producto}: "))
    monto_cliente = float(input("Ingrese el monto con el que va a pagar: "))
    
    resultado = tienda.vender_producto(nombre_producto, cantidad, monto_cliente)
    print(resultado)

# Función para gestionar recepción de productos de proveedores
def gestionar_proveedores(tienda):
    print("\n--- Gestión de Productos para Proveedores ---")
    nombre_producto = input("Ingrese el nombre del producto que entrega el proveedor: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre_producto} entregado: "))
    precio_sugerido = float(input(f"Ingrese el precio sugerido de venta para {nombre_producto}: "))
    
    resultado = tienda.recibir_proveedor(nombre_producto, cantidad, precio_sugerido)
    print(resultado)

# Uso del sistema de tienda
tienda = Tienda()

# Inventario inicial de productos de la canasta básica
productos_canasta_basica = [
    ("Arroz", 1.25, 100),
    ("Frijoles", 1.50, 80),
    ("Azúcar", 1.00, 150),
    ("Harina", 1.25, 60),
    ("Aceite", 2.50, 40),
    ("Leche", 1.20, 50),
    ("Huevos", 5.00, 200),  # Precio por Libra
    ("Sal", 1.05, 100),
    ("Mantequilla", 1.50, 40),
    ("Café", 3.00, 30)
]

# Agregar productos de la canasta básica al inventario
for nombre, precio, cantidad in productos_canasta_basica:
    tienda.agregar_producto(nombre, precio, cantidad)

# Opciones para el usuario
while True:
    print("\nSeleccione una opción:")
    print("1. Comprar producto (Cliente)")
    print("2. Entregar producto (Proveedor)")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        gestionar_compras(tienda)
    elif opcion == "2":
        gestionar_proveedores(tienda)
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
