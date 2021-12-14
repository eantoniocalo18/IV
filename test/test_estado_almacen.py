import pytest
from assertpy import assert_that
from funciones_test import *
from src.producto import Producto
from src.inventario import Inventario

def test1():
    # Cargamos productos
    productos = products_from_CSV('test/data.txt')
    
    # Cargamos el almacen
    almacen = almacen_from_CSV('test/data.txt')
    
    # Creamos un inventario
    inventario = Inventario(1,almacen,100)
    
    # Comprobamos que ambos NO están vacíos
    assert_that(productos).is_not_empty()
    assert_that(almacen).is_not_empty()
    
    # Comprobamos que el espacio es >0 y < dimensiones del almacen
    assert_that(inventario.get_espacio_usado()).is_greater_than(0)
    #print (inventario.get_dimensiones())
    assert_that(inventario.get_espacio_usado()).is_less_than(inventario.get_dimensiones())
    
