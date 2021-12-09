# Gestor de tareas
Invoke es una herramienta y biblioteca de ejecución de tareas de Python. Es similar a Rake en Ruby. Sigue en desarrollo y la última versión fue lanzada en Julio 2021.
Además, tal y como indica el guión del Objetivo 3, el gestor de tareas más usado para proyectos Python.
Esta herramienta permite automatizar tareas de una manera rápida creando archivos task.py

# Gestor de dependencias
Se han barajado varias alternativas cuyas principales ventajas/desventajas son:
  - Easy Install: Es incluido setuptools que permite descargar, construir, instalar y administrar paquetes de Python automáticamente. Fue lanzado en 2004 y está obsoleto.
  - Pip: Ofrece los mismos servicios que el anterior pero además permite desinstalar paquetes y sobreescribir dependencias.
  - Poetry: Un gestor de dependencias y un empaquetador de librerías python.
El gestor de dependencias que se va a usar es Poetry. La principal ventaja que presenta es que permite coordinar versiones de librerías, versiones de python y también versiones de los distintos frameworks para instalar exactamente las versiones para las que el proyecto funciona y no se creen conflictos.

