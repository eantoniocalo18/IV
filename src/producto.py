#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Producto.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 20/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------
import time


class Producto:
    """
    Clase utilizada para representar un Producto de Supermercado.
    ...

    Atributos
    ----------
   
    Publicos

    id: str
        uuid o id que identifica cada producto como único
    nombre : str
        el nombre común del producto
    precio : float
        el precio del producto

    Métodos


    -------
    
    """
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    
