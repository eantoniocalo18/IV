
# CUPONAPP

  
  

# Descripción

Los supermercados tienen encargados para gestionar sus almacenes que tienen que tener en cuenta infinidad para que todo funcione correctamente.

Es por ello, que una aplicación que le permita gestionar de manera eficiente el stock de los productos (no haya en exceso ni falta), le permita realizar pedidos de productos de manera automática y que además, gestione el inventario de manera que se pueda observar en tiempo real qué productos hay, podría solucionar muchos de los problemas a los que se tendría que enfrentar dicho usuario.

  

# Motivación

La idea del proyecto está basada en resolver los principales problemas a los que se puede enfrentar un gestor de almacen:

- En un almacen se quiere evitar bajo cualquier concepto perder productos porque su fecha de consumo preferente pase.

- La capacidad de almacenamiento es finita, por lo que no se pueden pedir exceso de productos

- Por otro lado, hay productos que se venden normalmente y cuyo pedido se repite cada cierto tiempo, por lo que sería muy útil que se pidieran solos

- Además, sería muy útil recibir la estadística del historial de ventas de cada producto para estimar el tiempo para la próxima compra y la cantidad necesaria

  
# Guía de instalación y uso
En primer lugar habrá que descargar el proyecto desde este repositorio, usando la orden:
  - git clone git@github.com:eantoniocalo18/IV

Para la instalación del proyecto, será necesario tener descargado el software Poetry [aquí] (https://python-poetry.org/docs/)
En el caso de sistemas Unix se podrá utilizar el siguiente comando 
  - curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
Una vez instalado, para comprobar que efectivamente está funcionando, usaremos la orden 
  - poetry --version

En el caso que nos aparezca que no se ha encontrado la orden "poetry" puede deberse a que no se ha añadido correctamente al $PATH del sistema. 
Para solucionar esto, consultar [aquí] (docs/poetry_problems.md)

Una vez comprobado que Poetry funciona correctamente, seguiremos los siguientes pasos:
  - poetry install --> Instalará todas las dependencias del proyecto
  - poetry shell --> Abrirá una terminal para poder ejecutar las diferentes tareas del proyecto
  Una vez abierto el nuevo entorno, podremos usar las órdenes:
    - invoke check --> Comprobará la sintaxis del archivo producto.py
    - invoke test --> Ejecutará los test del proyecto

   

## Documentación

  

La documentación del proyecto se encuentra en el archivo en [este enlace](https://github.com/eantoniocalo18/IV/tree/main/docs)

 - En el archivo [Issues](https://github.com/eantoniocalo18/IV/docs/ISSUES.md) se encuentra la información relacionada con los tipos de usuario, las historias de usuario y los milestones
 - En el archivo [Eleccion lenguaje](https://github.com/eantoniocalo18/IV/docs/eleccion_lenguaje.md) se encuentra la información relacionada con la elección del lenguaje y el desarrollo de la clase Producto.
 - En el archivo [Eleccion gestores] (https://github.com/eantoniocalo18/IV/docs/eleccion_gestores.md) Se ha justificado la elección de los gestores de dependencias y tareas.
