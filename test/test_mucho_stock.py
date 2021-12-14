import pytest
from assertpy import assert_that
from funciones_test import *
from src.producto import Producto
from src.inventario import Inventario

def test_poco_stock():
    # Cargamos productos
    productos = products_from_CSV('test/data.txt')
    
    # Cargamos el almacen
    almacen = almacen_from_CSV('test/data.txt')
    
    # Creamos un inventario
    inventario = Inventario(1,almacen,100)
    
    for products in almacen.items():
        c_max=int(products[0].get_cantidad_alta())
        assert_that(int(products[1])).is_less_than_or_equal_to(c_max)
 
