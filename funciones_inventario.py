import json
import csv
def registrarProducto(inventario):
    """registra producto nuevo ingresado por el usuario
       recibe el inventario para agregarle producto, cantidad y precio
    """
    nuevo_producto = []
    nuevo_producto.append(input("ingrese producto\n"))
    nuevo_producto.append(int(input("ingrese la cantidad\n")))
    nuevo_producto.append(int(input("ingrese precio por unidad\n")))
    inventario.append(nuevo_producto)
    print("---producto agregado en el inventario---")
    
    
def agregarProducto(inventario):
    """agrega producto a inventario existente
    recibe el inventario como argumento y lo modifica con el input del usuario
    """
    for item in inventario:
            print(item[0])
            
    selecion = input("seleciona producto a agregar existencias\n")
    
    #si el producto ya esta en el inventario agrega existencias sino crea el producto 
    if selecion in inventario:
        for item in inventario:
            
                if item[0]==selecion:
                    cantidad_agregar = int(input("ingrese cantidad a agregar\n"))
                    print(cantidad_agregar)
                    cantidad = int(item[1]) + cantidad_agregar
                    item[1]=cantidad 
                    print("---cantidad del producto actualizada en el inventario---")    
             
    else:
        print("el productono esta en elinventario AGREGUELO")
        registrarProducto(inventario)  
        
        
def restarInventario(inventario):
    """resta a articulos existente cantidad vendida
       modifica el inventario restanto la cantidad ingresada por el usuario
    """   
    #muetra productos en el inventario para selecionarlo
    for item_inventario in inventario:        
        print(item_inventario[0])    
    producto_vender = input("selecione producto a vender\n")
           
    for item_inventario in inventario:
        if producto_vender == item_inventario[0]:
            cantidad_descontar = int(input("ingrese cantidad a vender\n"))
            #si no hay existencias del producto selecionado se sale de la venta
            if item_inventario[1] - cantidad_descontar <= 0:
                print(f"NO hay existencias suficientes de {item_inventario[0]} ")
                break
            else:
                        
                cantidad = item_inventario[1]- cantidad_descontar
                item_inventario[1]=cantidad         
        
def imprimiInventario(inventario):
    print("INVENTARIO GENERAL")
    for item in inventario:
        print(f"producto:  {item[0]}  cantidad:  {item[1]}  precio :  {item[2]} ") 
        
        
def a_dicionario(inventario):
    dcionario_inventario = {}
    articulo = {}
    codigo = 1.1
    for item in inventario:
        articulo = dict(producto = item[0],cantidad=item[1],precio=item[2])
        dcionario_inventario[codigo]=articulo 
        codigo = codigo + 1
    print(dcionario_inventario)
    return dcionario_inventario        
    
def totalProductoInventario(inventario):
    """ 
    recibe el inventario totaliza por producto y  suma totales para totalizar el inventario
    """
    valor_total_inventario = 0
    print("INVENTARIO PARCIAL")
    for producto in inventario:
        total_producto = producto[1]*producto[2]
        valor_total_inventario = valor_total_inventario + total_producto
        
        print(f"{producto[0]} : {producto[1]} x {producto[2]}= {total_producto}") 
    print(f"el valor total del inventario es : {valor_total_inventario}")  
                    
def exportar_inventario(inventario):
    print("selecione formato de exportacion\n")
    formato = input("1-exportar como jason\n2-exportar como archivo plano\n3-exportar como hoja de calculo\n")
    dicionario =  a_dicionario(inventario)
    
    if formato == "1":
        print("json")
        
        with open("C:\\Users\\dfb\\Desktop\\curso python\\practica\\inventario_enca24\\archivo_inventariojson","w") as archivo:
            json.dump(dicionario,archivo,indent=4,ensure_ascii=False)
              
           
    if formato == "2":
        print("texto plano") 
        for elemento in inventario:
            producto = elemento[0]
            cantidad =  elemento[1]
            precio = elemento[2]
            item = "producto:     {}       cantidad :   {}   precio:   {}   \n".format(producto,cantidad,precio)     
            with open("C:\\Users\\dfb\\Desktop\\curso python\\practica\\inventario_enca24\\archivo_inventario.txt","a") as archivo:
                archivo.write(item)
           
    if formato == "3":
        print("archivo en hoja de calculo")
        with open("C:\\Users\\dfb\\Desktop\\curso python\\practica\\inventario_enca24\\archivo_hoja_calculo.csv","a",newline="") as archivo_cvs:
            escritor = csv.writer(archivo_cvs)
            escritor.writerows(inventario)    
            