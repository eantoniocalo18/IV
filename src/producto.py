# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Producto.
#----------------------------------------------------------------------------
# @author: Silvio Orozco @sorozcov 
# @created_date: 20/11/2021
# @version: '1.0'
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
    cantidad : int
        cantidad del producto que se encuentra disponible
    cantidad_bajo_inventario: int
        cantidad mínima de inventario para generar un aviso de bajo inventario
    cantidad_alto_inventario: int
        cantidad máxima de inventario para generar un aviso de alto inventario
    cantidad_ultimo_pedido: int
        cantidad solicitada en el ultimo pedido
    
    Privadas

    total_ventas: int
        cantidad total vendida del producto desde cierta fecha
    fecha_total_ventas: date
        fecha desde ultima actualizacion de total ventas a 0


    Métodos

    venta:
        Método que elimina una cantidad de producto al ser vendido y añade al total de ventas. Revisa si es necesario generar un aviso.
    avastecimiento:
        Método que añade una cantidad de producto al ser abstecido de un nuevo pedido y actualiza la cantidad de ultimo pedido. Revisa si es necesario generar un aviso.
    revisar_aviso_stock:
        Método que revisa la cantidad de stock del producto y la compara con la cantidad máxima de inventario o la cantidad mínima de inventario para generar un aviso si fuese necesario.
    resetear_ultimas_ventas:
        Método que setea la fecha de últimas ventas al momento actual y setea el total de ventas para esta nueva fecha en 0.
    mostrar_ultimas_ventas:
        Método que muestras la cantidad total de ventas desde la última fecha propuesta.
    frecuencia_compra:
        Método que devuelve la frecuencia de compra de las últimas ventas.
    -------
    
    """
    def __init__(self, id, nombre, precio,cantidad, cantidad_bajo_inventario,cantidad_alto_inventario):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.cantidad_bajo_inventario = cantidad_bajo_inventario
        self.cantidad_alto_inventario = cantidad_alto_inventario
        self.total_ventas = 0
        self.fecha_total_ventas = time.now()
    
    def venta(cantidad):
        """
        Método que elimina una cantidad de producto al ser vendido y añade al total de ventas. Revisa si es necesario generar un aviso.
        """

    def avastecimiento(cantidad):
        """
        Método que añade una cantidad de producto al ser abstecido de un nuevo pedido y actualiza la cantidad de ultimo pedido. Revisa si es necesario generar un aviso.
        """

    def revisar_aviso_stock():
        """
        Método que revisa la cantidad de stock del producto y la compara con la cantidad máxima de inventario o la cantidad mínima de inventario para generar un aviso si fuese necesario.
        Se debe llamar siempre luego de una venta o avastecimiento.
        """
    
    def resetear_ultimas_ventas():
        """
        Método que setea la fecha de últimas ventas al momento actual y setea el total de ventas para esta nueva fecha en 0.
        """

    def mostrar_ultimas_ventas():
        """
        Método que muestras la cantidad total de ventas desde la última fecha propuesta.
        """

    def frecuencia_compra():
        """
        Método que devuelve la frecuencia de compra de las últimas ventas.
        total_ventas/(fecha_actual-fecha_total_ventas)
        """