#----------------------------------------------------------------------------
# Este archivo Inventario.py contiene la implementación de la clase Inventario.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 22/11/2021
# @version: '1.0'
# --------------------------------------------------------------------------
from src.producto import *

class Inventario:
    """
    Clase utilizada para representar un Inventario de Supermercado.
    ...

    Atributos
    ----------
   
    Publicos

    almacen : {producto.id: { cantidad: cantidad, frecuencia:frecuencia}}
        Un diccionario de productos con los respectivos datos (producto, cantidad,frecuencia)
    dimensiones: 
    	Dimensiones medidas en m2 que tiene de espacio el almacen
    	
    Métodos
    venta:
        "Método que elimina cantidad de productos del inventario por una venta"
    
    abastecimiento:
        "Método que agrega una cantidad de producto al inventario"

    perdida:
         "Método que elimina cantidad de productos del inventario por una perdida del producto de algún tipo"
    


    -------
    """
    def __init__(self, id, almacen, dimensiones):
        self.id = id
        self.almacen = almacen
        self.dimensiones= dimensiones
        

    def venta(producto, cantidad):
        "Método que elimina cantidad de productos del inventario por una venta"
        pass
    
    def abastecimiento(producto,cantidad):
        "Método que agrega una cantidad de producto al inventario"
        pass

    def perdida(producto, cantidad):
        "Método que elimina cantidad de productos del inventario por una perdida del producto de algún tipo"
        pass
    
    def get_espacio_usado(self):
        espacio_ocupado=0
        for products in self.productos_dict.items():
             espacio_ocupado += (float(products[0].get_espacio()) * float(products[1]))

        return espacio_ocupado
        
    def get_dimensiones(self):
        return self.dimensiones
         
         
         
         
         
