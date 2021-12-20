# Elección de la imagen base

Requisitos que debe cumplir la imagen:
- Versión de Python ^3.9
- Sistema con las menores dependencias posibles
- Imágenes pequeñas
- Tiempo de ejecución para los test del proyecto


- Imagen oficial Python Docker:
Ventajas: 
	- Tiene preinstaladas múltiples veriones de Python.
	- Tiene varias variantes.
Desventajas:
	- La mayoría de sus variantes cuentan con una serie de paquetes comunes instalados cosa que no nos interesa pues queremos estrictamente los más necesarios.
	- La slim, variante de Debian 11, tiene menos paquetes pero depende de otras imágenes por lo que acaba ocupando más disco
	- Sus tamaños sin comprimir son entre 45 MB y 122MB
	
Dentro de las versiones oficiales de Python 3.9 slim tenemos :
- Python 3.9 slim
- Python 3.9 slim bullseye

El principal motivo para descartar la slim ha sido que tiene 82 [vulnerabilidades](https://snyk.io/test/docker/python%3A3.9.2-slim) conocidas de las cuales 22 son de riesgo alto.

Otros dockers que se han valorado como alternativa :
	- Debian 11
	- RHEL 8
Todos incluían la versión 3.8 y 3.9 de Python pero instalan otros paquetes que no son necesarios para el proyecto y por lo tanto su peso es mayor.

| Imagen | Tamaño | Ejecución de test | 
| ------------- | ------------- | ------------- |
| python:3.9-slim-bullseye | 174MB | 0.05s |
| debian:bullseye  | 422MB | 0.0.5s | 
| s2i-base:rhel8.5  | 502 MB |   X s  |



*No se han ejecutado los test con RHEL8 puesto que la diferencia de tamaño ya me hace descartala




Por lo tanto, viendo que desde el Docker oficial de Python podemos usar una versión 'slim' que ocupa 422 MB y además podemos elegir la versión específica que 
vamos a usar de Python, vamos a desplegar el docker basándonos en la imagen:
debian: python:3.9-slim-bullseye dado que cumple todos los requisitos establecidos y ofrece mejores resultados en la práctica.
