import csv
from src.producto import Producto
# Función que leerá los datos de un fichero CSV y los pasará a un diccionario de productos

def almacen_from_CSV(path):
    with open(path, mode='r') as csv_file:
        productos=products_from_CSV(path)
        csv_reader = csv.reader(csv_file) 
        diccionario = {}
        i=0
        for rows in csv_reader:
            diccionario[productos[i]]= rows[6]
            i+=1
    return diccionario


def products_from_CSV(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file) 
        listado_productos= []
        for rows in csv_reader:
            id= rows[0]
            nombre= rows[1]
            precio = rows[2]
            espacio = rows[3]
            cantidad_baja = rows[4]
            cantidad_alta = rows[5]
            producto = Producto(id,nombre,precio,espacio,cantidad_baja, cantidad_alta)
            listado_productos.append(producto)
    return listado_productos
    
    

