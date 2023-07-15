productos = []
carrito = []

#---------------------------------------------
def agregar_productos(cod, desc, stock, valor):
    item = {
        "codigo": cod,
        "desc"  : desc,
        "stock" : stock,
        "valor" : valor
    }
    productos.append(item)
#---------------------------------------------
def consultar_producto(cod):
    for item in productos:
        if item["codigo"] == cod:
            return item
    return False
#---------------------------------------------
def modificar_producto(cod, desc, stock, valor):
    for item in productos:
        if item["codigo"] == cod:
            item["desc"] = desc
            item["stock"] = stock
            item["valor"] = valor
            return True
    return False
#---------------------------------------------
def listar_productos():
    print("-"*30)
    for item in productos:
        print(f'Cod: {item["codigo"]} {item["desc"]}')
        print(f'Stock: {item["stock"]}')
        print(f'Valor: {item["valor"]}')
        print("-"*30)
#---------------------------------------------
# Funciones del carrito
#--------------------------------  -------------
def agregar_al_carrito(cod, cantidad):
    item = consultar_producto(cod)
    if item == False:
        print("El producto no existe")
        return False
    if cantidad > item["stock"]:
        print("Cantidad insuficiente")
        return False
    # Veo si hay que sumar a lo que ya tengo
    for articulo in carrito:
        if articulo["codigo"] == cod:
            articulo["stock"] += cantidad
            return True
    # Agrego item al carrito
    aux = {
        "codigo": cod,
        "desc"  : item["desc"],
        "stock" : cantidad,
        "valor" : item["valor"]
    }
    carrito.append(aux)
#---------------------------------------------
def quitar_del_carrito(cod, cant):
    for item in carrito:
        if item["codigo"] == cod:
            if cant>item["stock"]:
                print("No puedo descontar mas de lo que tengo!"  )
                return False
            item["stock"] -= cant

            if item["stock"] == 0:
                carrito.remove(item)
            return True
    print("Producto no existe en el carrito!")
    return False
    
#---------------------------------------------
def listar_carrito():
    total_a_pagar = 0
    print("-"*30)
    for item in carrito:
        print(f'Cod: {item["codigo"]} {item["desc"]}')
        print(f'Cantidad: {item["stock"]} Precio: {item["valor"]}')
        importe = item["stock"] * item["valor"]
        total_a_pagar += importe
        print(f'Importe: {importe}')
        print("-"*30)
    print(f"Total: {total_a_pagar}")
    print("-"*30)

print()
print()
agregar_productos(1, "Calathea", 10, 1500)
agregar_productos(2, "Ceropegia Woodi", 20, 1800)
agregar_productos(3, "Espatifilo", 15, 3000)
agregar_productos(4, "Ficus Lyrata", 17, 1500)
agregar_productos(5, "Maranta Leuconera", 20, 2000)
agregar_productos(6, "Monstera", 16, 4000)
agregar_productos(7, "Chamaedorea elegans", 18, 3500)
agregar_productos(8, "Cereus Preuvianus", 30, 600)
agregar_productos(9, "Graptopetalum", 20, 700)
agregar_productos(10, "Graptoveria", 15, 700)
agregar_productos(11, "Myrtillocactus", 9, 900)
agregar_productos(12, "Haworthia fasciata", 5, 800)






agregar_al_carrito(1, 5)
agregar_al_carrito(2, 1)
agregar_al_carrito(3, 3)

listar_productos()
listar_carrito()





print()
print()