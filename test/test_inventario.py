import pytest
from assertpy import assert_that
from .funciones_test import *
from src.producto import Producto
from src.inventario import Inventario

def test_estado_almacen():
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
    assert_that(inventario.get_espacio_usado(), description='El espacio del almacén tiene valores erróneos').is_less_than(inventario.get_dimensiones())


def test_mucho_stock():
    # Cargamos productos
    productos = products_from_CSV('test/data.txt')
    
    # Cargamos el almacen
    almacen = almacen_from_CSV('test/data.txt')
    
    # Creamos un inventario
    inventario = Inventario(1,almacen,100)
    
    for products in almacen.items():
        c_max=int(products[0].get_cantidad_alta())
        assert_that(int(products[1]),description='Hay cantidad alta de al menos un producto').is_less_than_or_equal_to(c_max)
        
def test_poco_stock():
    # Cargamos productos
    productos = products_from_CSV('test/data.txt')
    
    # Cargamos el almacen
    almacen = almacen_from_CSV('test/data.txt')
    
    # Creamos un inventario
    inventario = Inventario(1,almacen,100)
    
    for products in almacen.items():
        c_min=int(products[0].get_cantidad_baja())
        assert_that(int(products[1]),description='Hay cantidad baja de al menos un producto').is_greater_than(c_min)
        
