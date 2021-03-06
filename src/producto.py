#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Producto.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 20/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------


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
    dimensiones: float
        espacio (medido en cm cuadrados) que ocupa el objeto
    cantidad_baja: int
        entero que representará el número mínimo de productos que queremos tener en stock
    cantidad_alta: int
    	entero que representará el número máximo de productos que queremos tener en stock
    Métodos


    -------
    
    """
    def __init__(self, id, nombre, precio,espacio,cantidad_baja,cantidad_alta):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.espacio = espacio
        self.cantidad_baja= cantidad_baja
        self.cantidad_alta= cantidad_alta
        
        
    def get_espacio(self):
        return self.espacio
        
    def get_cantidad_baja(self):
        return self.cantidad_baja
        
    def get_cantidad_alta(self):
        return self.cantidad_alta    
        
        
        
