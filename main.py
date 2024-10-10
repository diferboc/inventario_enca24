from funciones_inventario import registrarProducto,agregarProducto,restarInventario,imprimiInventario,totalProductoInventario,a_dicionario,exportar_inventario
import datetime
 
fecha = datetime.datetime.now()
año = fecha.year
mes = fecha.month
dia = fecha.day
hora = fecha.hour
minutos = fecha.minute

print("---------INVENTARIO-TECNOFRUVER------")
print(f"fecha : {dia}-{mes}-{año}  hora: {hora}:{minutos}")
#inicializar inventario con 3 productos con su cantidad y precio
i = 0
inventario= []
while i < 3:
    registrarProducto(inventario)   
    i = i + 1


while True:
    opcion = input("selecione\n1-registrar producto/nombre/cantidad/precio\n2-agregar existencias\n3-vender cantidad expecifica\n4-listar todos los productos\n5-valor total del inventario\n6-a_dcionario\n7-exportar_inventario\n8-Salir\n")
    if opcion == "1":
        #crear lista para el registro del producto nuevo con su precio y cantidad,agregar a el inventario
        registrarProducto(inventario)
        
    elif opcion == "2":
        #agrega producto al inventario
        agregarProducto(inventario)

    elif opcion == "3":
        #resta producto al inventario
        restarInventario(inventario)
    elif opcion == "4":
        #muestra el inventario
        imprimiInventario(inventario)
        
    elif opcion =="5":
        #totales por producto y total del inventario 
        totalProductoInventario(inventario) 
    
    elif opcion == "6":
        a_dicionario(inventario)
        
    elif opcion == "7":
        exportar_inventario(inventario)    
        
    elif opcion == "8":
        #salida del bucle 
        break
    
    
                

