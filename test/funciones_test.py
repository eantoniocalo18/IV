import csv
from src.producto import Producto
# Función que leerá los datos de un fichero CSV y los pasará a un diccionario de productos

def almacen_from_CSV(path):
    with open(path, mode='r') as csv_file:
        productos=products_from_CSV(path)
        csv_reader = csv.reader(csv_file) 
        diccionario = {}
        #el diccionario tiene como clave un objeto de tipo Producto y de valor una cantidad
        i=0
        for rows in csv_reader:
        # Añadimos a la clave 'Producto' la cantidad de productos que tenemos
            diccionario[productos[i]]= rows[6]
            i+=1
    return diccionario


def products_from_CSV(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file) 
        listado_productos= []
        for rows in csv_reader:
            producto = Producto(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5])
            listado_productos.append(producto)
    return listado_productos
    
    

