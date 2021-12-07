#----------------------------------------------------------------------------
# Este archivo frecuencia_compra.py contiene la implementación de la clase FrecuenciaCompra.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 22/11/2021
# @version: '1.0'
# ---------------------------------------------------------------------------


class FrecuenciaCompra:
    """
    Clase utilizada para representar un FrecuenciaCompra de cantidad Supermercado.
    ...

    Atributos
    ----------
   
    Publicos

    producto : Producto
        contiene un producto
    cantidad_x_semana : int
        mantiene la cantidad de FrecuenciaCompra actual de un producto
    

    Métodos
    solicitar_frecuencia:
        "Método que dada una serie de ventas genera la cantidad de producto vendido x semana"
    

    realizar_pedido_automatizado:
         "Método que realiza un pedido cada semana según la frecuencia de compra"
    


    -------
    """
    def __init__(self, id, producto):
        self.id = id
        self.producto = producto
        self.cantidad_x_semana = 0

    def solicitar_frecuencia(ventas):
        "Método que dada una serie de ventas genera la cantidad de producto vendido x semana"
        pass
    


