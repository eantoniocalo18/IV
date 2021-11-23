#----------------------------------------------------------------------------
# Este archivo Venta.py contiene la implementación de la clase Venta.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 22/11/2021
# @version: '1.0'
# ---------------------------------------------------------------------------
import time


class Venta:
    """
    Clase utilizada para representar un Venta de Supermercado.
    ...

    Atributos
    ----------
   
    Publicos

    producto : Producto
        contiene un producto
    cantidad : int
        la cantidad vendida
    fecha: Date
        la fecha que se realizó la venta
    

    Métodos



    -------
    """
    def __init__(self, id, producto, cantidad):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad

