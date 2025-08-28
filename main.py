class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre
class Manejo_Categoria:
    def __init__(self):
        self.categorias={}
        self.cargar_categoria()
    def cargar_categoria(self):
        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        id_categoria, nombre=linea.split(":")
                        self.categorias[id_categoria]=Categoria(id_categoria, nombre)
            print("Categorias importadas satisfactoriamente desde: 'categoria.txt'")
        except FileNotFoundError:
            print("No hay archivo para categoria, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_categoria(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for id_categoria, datos in self.categorias.items():
                archivo.write(f"{id_categoria}:{datos['nombre']}")
    def agregar_categoria(self, id_categoria, nombre):
        if id_categoria in self.categorias.keys():
            print("Ese ID de categoria ya se encuentra registrado...")
            return
        self.categorias[id_categoria]=Categoria(id_categoria, nombre)
        self.guardar_categoria()
        print(f"Categoria: {nombre} agregada con exito...")

    def modificar_categoria(self, id_categoria, nuevo_nombre):
        if id_categoria not in self.categorias:
            print(f"No existe una categoría con ID {id_categoria}.")
            return
        self.categorias[id_categoria].nombre = nuevo_nombre
        self.guardar_categoria()
        print(f"Categoría {id_categoria} modificada a '{nuevo_nombre}'.\n")

    def eliminar_categoria(self, id_categoria):
        if id_categoria not in self.categorias:
            print(f"No existe una categoría con ID {id_categoria}.")
            return
        nombre = self.categorias[id_categoria].nombre
        del self.categorias[id_categoria]
        self.guardar_categoria()
        print(f"Categoría '{nombre}' eliminada con éxito.\n")

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
        self.id_categoria=id_categoria
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock

class Manejo_Producto:
    def __init__(self):
        self.productos={}
        self.cargar_productos()
    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        id_productos, nombre, precio, id_categoria, total_compras, total_ventas, stock=linea.split(":")
                        self.productos[id_productos]=Producto(id_productos, nombre, precio, id_categoria, total_compras, total_ventas, stock)
            print("Productos importados satisfactoriamente desde: 'productos.txt'")
        except FileNotFoundError:
            print("No hay archivo para productos, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for id_productos, datos in self.productos.items():
                archivo.write(f"{id_productos}:{datos['nombre']}:{datos['precio']}:{datos['id_categoria']}:{datos['total_compras']}:{datos['totao_ventas']:{datos['stock']}}")
    def agregar_productos(self, id_productos, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        if id_productos in self.productos.keys():
            print("Este producto ya se encuentra registrado, intente de nuevo...")
            return
        self.productos[id_productos]=Producto(id_productos, nombre, precio, id_categoria, total_compras, total_ventas, stock)
        self.guardar_productos()
        print(f"Producto: '{nombre}' agregado con exito\n")
    def modificar_productos(self, id_productos, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
        if id_productos not in self.productos.keys():
            print("El producto no esta registrado, intente de nuevo...")
            return
        producto=self.productos[id_productos]
        if nuevo_nombre is not None:
            producto.nombre=nuevo_nombre
        if nuevo_precio is not None:
            producto.precio=nuevo_precio
        if nuevo_stock is not None:
            producto.stock=nuevo_stock
        self.guardar_productos()

        print(f"Producto: {producto.nombre} actualizado con exito. \n")


class Clientes:
    def __init__(self):
        self.clientes={}
        self.cargar_clientes()
    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo=linea.split(":")
                        self.clientes[nit]={"nombre":nombre, "direccion":direccion, "telefono":telefono, "correo":correo}
            print("Clientes importados satisfactoriamente desde: 'clientes.txt'")
        except FileNotFoundError:
            print("No hay archivo para clientes, se creara uno nuevo cuando se guarden datos automaticamente")
class Proveedores:
    def __init__(self):
        self.proveedores={}
        self.cargar_proveedores()
    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo, empresa=linea.split(":")
                        self.proveedores[nit]={"nombre": nombre, "direccion":direccion, "telefono":telefono, "correo":correo, "empresa":empresa}
            print("Proveedores importados satisfactoriamente desde: 'proveedores.txt'")
        except FileNotFoundError:
            print("No hay archivo para proveedores, se creara uno nuevo cuando se guarden datos automaticamente")
class Empleados:
    def __init__(self):
        self.empleados={}
        self.cargar_empleados()
    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        id_empleado, nombre, direccion, telefono, correo, puesto=linea.split(":")
                        self.empleados[id_empleado]={"nombre": nombre, "direccion":direccion, "telefono":telefono, "correo":correo, "puesto":puesto}
            print("Categoria importada satisfactoriamente desde: 'empleados.txt'")
        except FileNotFoundError:
            print("No hay archivo para empleados, se creara uno nuevo cuando se guarden datos automaticamente")
class Ventas:
    def __init__(self):
        self.ventas={}
        self.cargar_ventas()
    def cargar_ventas(self):
        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        id_venta, fecha, id_empleado, nit, total=linea.split(":")
                        self.ventas[id_venta]={"fecha":fecha, "id_empleado":id_empleado, "nit":nit, "total":total}
            print("Ventas importadas satisfactoriamente desde: 'ventas.txt'")
        except FileNotFoundError:
            print("No hay archivo para ventas, se creara uno nuevo cuando se guarden datos automaticamente")
class Detalle_Ventas:
    def __init__(self):
        self.detalle_ventas={}
    def cargar_detalle_ventas(self):
        try:
            with open("detalleventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        id_detalle_ventas, id_venta, cantidad, id_producto, subtotal, stock=linea.split(":")
                        self.detalle_ventas[id_detalle_ventas]={"id_venta":id_venta, "cantidad":cantidad, "id_producto":id_producto, "subtotal":subtotal, "stock":stock}
            print("Detalle de ventas importado satisfactoriamente desde: 'detalleventas.txt")
        except FileNotFoundError:
            print("No hay archivo para detalle de ventas, se creara uno nuevo cuando se guarden datos automaticamente")

categorias = {}
productos = {}

while True:
    print("\n--- Menú ---")
    print("1. Agregar categoría")
    print("2. Agregar producto")
    print("3. Listar categorías")
    print("4. Listar productos")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        idc = input("IDCategoria: ")
        nombre = input("Nombre categoría: ")
        categorias[idc] = Categoria(idc, nombre)
        print("Categoría agregada.")

    elif opcion == "2":
        idp = input("IDProducto: ")
        nombre = input("Nombre producto: ")
        precio = float(input("Precio: "))
        idc = input("IDCategoria del producto: ")

        if idc not in categorias:
            print("Error: La categoría no existe. Agrega primero la categoría.")
        else:
            stock = int(input("Stock inicial: "))
            productos[idp] = Producto(idp, nombre, precio, idc, stock=stock)
            print("Producto agregado.")

    elif opcion == "3":
        if not categorias:
            print("No hay categorías.")
        for c in categorias.values():
            print(f"[{c.id_categoria}] {c.nombre}")

    elif opcion == "4":
        if not productos:
            print("No hay productos.")
        for p in productos.values():
            cat = categorias[p.id_categoria]
            print(f"[{p.id_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {cat.nombre} | Stock: {p.stock}")

    elif opcion == "5":
        break
    else:
        print("Opción inválida")