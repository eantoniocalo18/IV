# Elección de la imagen base

##Requisitos que debe cumplir la imagen:
- Versión de Python ^3.9
- Sistema con las menores dependencias posibles
- Imágenes pequeñas


- Imagen oficial Python Docker:
Ventajas: 
	- Tiene preinstaladas múltiples veriones de Python.
	- Tiene varias variantes.
Desventajas:
	- La mayoría de sus variantes cuentan con una serie de paquetes comunes instalados cosa que no nos interesa pues queremos estrictamente los más necesarios.
	- La slim, variante de Debian 11, tiene menos paquetes pero depende de otras imágenes por lo que acaba ocupando más disco
	- Sus tamaños sin comprimir son entre 45 MB y 122MB

Por lo tanto, viendo que desde el Docker oficial de Python podemos usar una versión 'slim' que puede ocupar 45 MB y además podemos elegir la versión específica que 
vamos a usar de Python, vamos a desplegar el docker basándonos en la imagen:
debian: python:3.9-slim-bullseye dado que cumple todos los requisitos establecidos.

Otros dockers que se han valorado han sido:
	- Debian 11
	- Ubuntu 20.04 
	- RHEL 8
Todos incluían la versión 3.8 y 3.9 de Python pero instalan otros paquetes que no son necesarios para el proyecto y por lo tanto su peso es mayor.

