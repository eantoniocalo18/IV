#----------------------------------------------------------------------------
# Este archivo Inventario.py contiene la implementación de la clase Inventario.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 22/11/2021
# @version: '1.0'
# ---------------------------------------------------------------------------
import time


class Inventario:
    """
    Clase utilizada para representar un Inventario de Supermercado.
    ...

    Atributos
    ----------
   
    Publicos

    producto : Producto
        contiene un producto
    cantidad : int
        mantiene la cantidad de inventario actual de un producto
    

    Métodos
    venta:
        "Método que elimina cantidad de productos del inventario por una venta"
    
    abastecimiento:
        "Método que agrega una cantidad de producto al inventario"

    perdida:
         "Método que elimina cantidad de productos del inventario por una perdida del producto de algún tipo"
    


    -------
    """
    def __init__(self, id, producto, cantidad):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad

    def venta(cantidad):
        "Método que elimina cantidad de productos del inventario por una venta"
    
    def abastecimiento(cantidad):
        "Método que agrega una cantidad de producto al inventario"

    def perdida(cantidad):
        "Método que elimina cantidad de productos del inventario por una perdida del producto de algún tipo"
