#Dependencias


## Gestor de dependencias

Para el correcto desarrollo del proyecto se necesita un sotfware que permita al usuario final o a un desarrollador instalar todas las dependencias necesarias para ejecutarlo.
Para llevar a cabo esta tarea se ha elegido el gestor de dependencias Poetry, un gestor de 
dependencias y un empaquetador de librerías python. 

La principal ventaja que presenta es que permite coordinar versiones de librerías, versiones de python y también versiones de los distintos frameworks para instalar exactamente las versiones para las que el proyecto funciona y no se creen conflictos.

## Funcionamiento

Para llevar a cabo la instalación de dependencias usando Poetry solo necesitamos ejecutar la orden:

    - poetry install

Con esto, ya tendríamos las dependencias instaladas. Sin embargo, estas dependencias estarían instaladas en un entorno virtual propio que crea poetry.
Esto nos supone un problema, puesto que las pruebas que se van a realizar al código van a ser en un entorno virtualizado (un dokcer) y por otra parte la instalación con Poetry nos creará un nuevo entorno virtualizado. 
Es por ello, que tenemos que pasarle el flag 'virtual.envs=False', para que Poetry no instale las dependencias en su propio entorno virtual sino en el entorno que nosotros estamos trabajando.