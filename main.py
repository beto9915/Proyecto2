class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock
class Clientes:
    def __init__(self, nit_cliente, nombre_cliente, direccion_cliente, telefono_cliente, correo_cliente):
        self.nit_cliente=nit_cliente
        self.nombre_cliente=nombre_cliente
        self.direccion_cliente=direccion_cliente
        self.telefono_cliente=telefono_cliente
        self.correo_cliente=correo_cliente
        self.clientes={}
class Proveedores:
    def __init__(self, nit_proveedor, nombre_proveedor, direccion_proveedor, telefono_proveedor, correo_proveedor, empresa):
        self.nit_proveedor=nit_proveedor
        self.nombre_proveedor=nombre_proveedor
        self.direccion_proveedor=direccion_proveedor
        self.telefono_proveedor=telefono_proveedor
        self.correo_proveedor=correo_proveedor
        self.empresa=empresa
        self.proveedores={}
class Empleados:
    def __init__(self, id_empleado, nombre_empleado, direccion_empleado, telefono_empleado, correo_empleado, puesto):
        self.id_empleado=id_empleado
        self.nombre_empleado=nombre_empleado
        self.direccion_empleado=direccion_empleado
        self.telefono_empleado=telefono_empleado
        self.correo_empleado=correo_empleado
        self.puesto=puesto
        self.empleados={}
class Ventas:
    def __init__(self, id_ventas, fecha, id_empleado, nit_cliente, total):
        self.id_ventas=id_ventas
        self.fecha=fecha
        self.id_empleado=id_empleado
        self.nit_cliente=nit_cliente
        self.total=total
        self.ventas={}

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