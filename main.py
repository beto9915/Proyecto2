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
    def eliminar_productos(self, id_productos):
        if id_productos not in self.productos.keys():
            print("El producto no existe...")
            return
        producto=self.productos[id_productos]
        del(producto)
        self.guardar_productos()
        print(f"El producto {producto.nombre} se elimino correctamente...")
class Clientes:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit=nit
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo

class Manejo_Clientes:
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
                        self.clientes[nit]=Clientes(nit, nombre,direccion, telefono,correo)
            print("Clientes importados satisfactoriamente desde: 'clientes.txt'")
        except FileNotFoundError:
            print("No hay archivo para clientes, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(f"{nit}:{datos["nombre"]}:{datos["direccion"]}:{datos["telefono"]}:{datos["correo"]}")
        print("Cliente guardado satisfactoriamente...")
    def agregar_cliente(self, nit, nombre, direccion, telefono, correo):
        if nit  in self.clientes.keys():
            print("El cliente ya se encuentra registrado...")
            return
        self.clientes[nit]=Clientes(nit, nombre, direccion, telefono, correo)
        self.guardar_clientes()
        print("Cliente registrado con exito...")
    def modificar_cliente(self, nit,nuevo_nit=None, nuevo_nombre=None, nueva_direccion=None, nuevo_telefono=None, nuevo_correo=None):
        if nit not in self.clientes.keys():
            print("El cliente no existe...")
            return
        cliente=self.clientes[nit]
        if nuevo_nit is not None:
            cliente.nit=nuevo_nit
        if nuevo_nombre is not None:
            cliente.nombre=nuevo_nombre
        if nueva_direccion is not None:
            cliente.direccion=nueva_direccion
        if nuevo_telefono is not None:
            cliente.telefono=nuevo_telefono
        if nuevo_correo is not None:
            cliente.correo=nuevo_correo
        print("El cliente fue modificado con exito...")
        self.guardar_clientes()
    def eliminar_cliente(self, nit):
        if nit not in self.clientes.keys():
            print("El cliente no esta registrado...")
            return
        cliente=self.clientes[nit]
        del(cliente)
        self.guardar_clientes()
        print("El cliente fue eliminado con exito...")
class Proveedores:
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        self.nit=nit
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
        self.empresa=empresa

class Manejo_Proveedores:
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
                        self.proveedores[nit]=Proveedores(nit, nombre, direccion, telefono, correo, empresa)
            print("Proveedores importados satisfactoriamente desde: 'proveedores.txt'")
        except FileNotFoundError:
            print("No hay archivo para proveedores, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.proveedores.items():
                archivo.write(f"{nit}:{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}:{datos['empresa']}")
        print("Proveedor guardado con exito en 'proveedores.txt'\n")
    def agregar_proveedor(self, nit, nombre, direccion, telefono, correo, empresa):
        if nit in self.proveedores.keys():
            print("El proveedor ya se encuentra registrado\n")
            return
        self.proveedores[nit]=Proveedores(nit, nombre, direccion, telefono, correo, empresa)
        self.guardar_proveedores()
        print(f"Proveedor {nombre} agregado con exito...\n")
    def modificar_proveedor(self, nit, nuevo_nit=None, nuevo_nombre=None, nueva_direccion=None, nuevo_telefono=None, nuevo_correo=None, nueva_empresa=None):
        if nit not in self.proveedores.keys():
            print("El proveedor no existe...\n")
            return
        proveedor=self.proveedores[nit]
        if nuevo_nit is not None:
            proveedor.nit=nuevo_nit
        if nuevo_nombre is not None:
            proveedor.nombre=nuevo_nombre
        if nueva_direccion is not None:
            proveedor.direccion=nueva_direccion
        if nuevo_telefono is not None:
            proveedor.telefono = nuevo_telefono
        if nuevo_correo is not None:
            proveedor.correo=nuevo_correo
        if nueva_empresa is not None:
            proveedor.empresa=nueva_empresa
        self.guardar_proveedores()
        print(f"El proveedor: {proveedor.nombre} actualizado con exito...\n")
    def eliminar_proveedor(self, nit):
        if nit not in self.proveedores.keys():
            print("El proveedor no existe...")
            return
        proveedor=self.proveedores[nit]
        del(proveedor)
        print(f"El proveedor {proveedor.nombre} se elimino con exito...")
        self.guardar_proveedores()
class Empleados:
    def __init__(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        self.id_empleado=id_empleado
        self.nombre-=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
        self.puesto=puesto
class Manejo_Empleados:
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
                        self.empleados[id_empleado]=Empleados(id_empleado, nombre, direccion, telefono, correo, puesto)
            print("Categoria importada satisfactoriamente desde: 'empleados.txt'")
        except FileNotFoundError:
            print("No hay archivo para empleados, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for id_empleado, datos in self.empleados.items():
                archivo.write(f"{id_empleado}:{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}:{datos['puesto']}")
    def agregar_empleado(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        if id_empleado in self.empleados.keys():
            print("Empleado ya esta registrado...")
            return
        self.empleados[id_empleado]=Empleados(id_empleado, nombre, direccion, telefono, correo, puesto)
        self.guardar_empleados()
        print("Empleado agregado con exito...")
    def modificar_empleado(self, id_empleado, nueva_direccion=None, nuevo_telefono=None, nuevo_correo=None):
        if id_empleado not in self.empleados.keys():
            print("Empleado no existe...")
            return
        empleado=self.empleados[id_empleado]
        if nueva_direccion is not None:
            empleado.direccion=nueva_direccion
        if nuevo_telefono is not None:
            empleado.telefono=nuevo_telefono
        if nuevo_correo is not None:
            empleado.correo=nuevo_correo
        self.guardar_empleados()
        print(f"El empleado: {empleado.nombre} fue actualizado con exito...")
    def eliminar_empleado(self, id_empleado):
        if id_empleado not in self.empleados.keys():
            print("Empleado no existe...")
            return
        empleado=self.empleados[id_empleado]
        del(empleado)
        self.guardar_empleados()
        print(f"Empleado: {empleado.nombre} eliminado con exito...")
class Ventas:
    def __init__(self, id_venta, fecha, id_empleado, nit, total):
        self.id_venta=id_venta
        self.fecha=fecha
        self.id_empleado=id_empleado
        self.nit=nit
        self.total=total
class Manejo_Ventas:
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
                        self.ventas[id_venta]=Ventas(id_venta, fecha, id_empleado, nit, total)
            print("Ventas importadas satisfactoriamente desde: 'ventas.txt'")
        except FileNotFoundError:
            print("No hay archivo para ventas, se creara uno nuevo cuando se guarden datos automaticamente")
    def guardar_ventas(self):
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for id_venta, datos in self.ventas.items():
                archivo.write(f"{id_venta}:{datos['fecha']}:{datos['id_empleado']}:{datos['nit']}:{datos['total']}")
        print("Venta guardada")
    def agregar_venta(self, id_venta, fecha, id_empleado, nit, total):
        self.ventas[id_venta]=Ventas(id_venta, fecha, id_empleado, nit, total)
        self.guardar_ventas()
        print("Venta guardada")
    def modificar_venta(self, id_venta, nueva_fecha=None, nuevo_nit=None, nuevo_total=None):
        if id_venta not in self.ventas.keys():
            print("Venta no existe")
            return
        venta=self.ventas[id_venta]
        if nueva_fecha is not None:
            venta.fecha=nueva_fecha
        if nuevo_nit is not None:
            venta.nit=nuevo_nit
        if nuevo_total is not None:
            venta.total=nuevo_total
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
    def guardar_detalle_ventas(self):
        with open("detalleventas.txt", "w", encoding="utp-8") as archivo:
            for id_detalle_ventas, datos in self.detalle_ventas.items():
                archivo.write(f"{id_detalle_ventas}:{datos['id_venta']}:{datos['cantidad']}:{datos['id_producto']}:{datos['subtotal']}:{datos['stock']}")
        print("Detalle de ventas guardado")
    def eliminar_detalle_ventas(self, id_detalle_ventas):
        if id_detalle_ventas not in self.detalle_ventas.keys():
            print("No existe ese detalle...")
            return
        detalle=self.detalle_ventas[id_detalle_ventas]
        del(detalle)
        self.guardar_detalle_ventas()
        print(f"Detalle de venta: {detalle.id_venta} eliminado con exito...")
class Program:
    @staticmethod
    def main():
        opcion = 0
        while opcion != 8:
            try:
                print("\n=== MENÚ PRINCIPAL ===")
                print("1. Ingrese Categoría")
                print("2. Ingrese Producto")
                print("3. Ingrese Cliente")
                print("4. Ingrese Proveedor")
                print("5. Ingrese Empleado")
                print("6. Registre Venta")
                print("7. Registre Detalle de Venta")
                print("8. Salir")
                opcion = int(input("Seleccione una opción: "))

                match opcion:
                    # =============================
                    case 1:  # Categoría
                        id_categoria = input("Ingrese el ID de categoría: ")
                        nombre = input("Ingrese el nombre: ")
                        categoria = Manejo_Categoria()
                        categoria.agregar_categoria(id_categoria, nombre)

                    # =============================
                    case 2:
                        categorias = Manejo_Categoria()
                        if not categorias.categorias:
                            print("No hay categorías registradas. Registre una categoría primero.")
                            continue
                        id_producto = input("Ingrese el ID de producto: ")
                        nombre = input("Ingrese el nombre del producto: ")
                        precio = input("Ingrese el precio: ")
                        id_categoria = input("Ingrese el ID de la categoría: ")
                        if id_categoria not in categorias.categorias:
                            print("La categoría ingresada no existe.")
                            continue
                        total_compras = input("Ingrese total de compras: ")
                        total_ventas = input("Ingrese total de ventas: ")
                        stock = input("Ingrese stock disponible: ")
                        producto = Manejo_Producto()
                        producto.agregar_productos(id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock)


                    case 3:
                        nit = input("Ingrese NIT del cliente: ")
                        nombre = input("Ingrese nombre: ")
                        direccion = input("Ingrese dirección: ")
                        telefono = input("Ingrese teléfono: ")
                        correo = input("Ingrese correo: ")
                        cliente = Manejo_Clientes()
                        cliente.agregar_cliente(nit, nombre, direccion, telefono, correo)


                    case 4:
                        nit = input("Ingrese NIT del proveedor: ")
                        nombre = input("Ingrese nombre: ")
                        direccion = input("Ingrese dirección: ")
                        telefono = input("Ingrese teléfono: ")
                        correo = input("Ingrese correo: ")
                        empresa = input("Ingrese empresa: ")
                        proveedor = Manejo_Proveedores()
                        proveedor.agregar_proveedor(nit, nombre, direccion, telefono, correo, empresa)


                    case 5:
                        id_empleado = input("Ingrese ID del empleado: ")
                        nombre = input("Ingrese nombre: ")
                        direccion = input("Ingrese dirección: ")
                        telefono = input("Ingrese teléfono: ")
                        correo = input("Ingrese correo: ")
                        puesto = input("Ingrese puesto: ")
                        empleado = Manejo_Empleados()
                        empleado.agregar_empleado(id_empleado, nombre, direccion, telefono, correo, puesto)


                    case 6:
                        # Validaciones
                        empleados = Manejo_Empleados()
                        clientes = Manejo_Clientes()
                        productos = Manejo_Producto()
                        if not empleados.empleados:
                            print("No hay empleados registrados. Registre un empleado primero.")
                            continue
                        if not clientes.clientes:
                            print("No hay clientes registrados. Registre un cliente primero.")
                            continue
                        if not productos.productos:
                            print("No hay productos registrados. Registre un producto primero.")
                            continue

                        id_venta = input("Ingrese ID de la venta: ")
                        fecha = input("Ingrese fecha (dd/mm/yyyy): ")
                        id_empleado = input("Ingrese ID del empleado que atiende: ")
                        if id_empleado not in empleados.empleados:
                            print("⚠ El empleado no existe.")
                            continue
                        nit = input("Ingrese NIT del cliente: ")
                        if nit not in clientes.clientes:
                            print("⚠ El cliente no existe.")
                            continue
                        total = input("Ingrese total: ")
                        venta = Manejo_Ventas()
                        venta.agregar_venta(id_venta, fecha, id_empleado, nit, total)


                    case 7:
                        ventas = Manejo_Ventas()
                        productos = Manejo_Producto()
                        if not ventas.ventas:
                            print("No hay ventas registradas. Registre una venta primero.")
                            continue
                        if not productos.productos:
                            print("No hay productos registrados. Registre un producto primero.")
                            continue

                        id_detalle = input("Ingrese ID del detalle: ")
                        id_venta = input("Ingrese ID de la venta: ")
                        if id_venta not in ventas.ventas:
                            print("La venta no existe.")
                            continue
                        id_producto = input("Ingrese ID del producto: ")
                        if id_producto not in productos.productos:
                            print("El producto no existe.")
                            continue
                        cantidad = int(input("Ingrese cantidad: "))
                        producto = productos.productos[id_producto]
                        if cantidad > int(producto.stock):
                            print("No hay suficiente stock disponible.")
                            continue
                        subtotal = float(producto.precio) * cantidad
                        stock_restante = int(producto.stock) - cantidad
                        detalle = Detalle_Ventas()
                        detalle.detalle_ventas[id_detalle] = {
                            "id_venta": id_venta,
                            "cantidad": cantidad,
                            "id_producto": id_producto,
                            "subtotal": subtotal,
                            "stock": stock_restante
                        }
                        detalle.guardar_detalle_ventas()
                        print("Detalle de venta registrado con éxito.")

                    case 8:
                        print("Saliendo del programa...")

                    case _:
                        print("Opción inválida, intente nuevamente.")

            except ValueError:
                print("Error, debe ingresar un número entero...")
