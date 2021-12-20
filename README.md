
# MANAGEAPP

  
  

## Descripción

Los supermercados tienen encargados para gestionar sus almacenes que tienen que tener en cuenta infinidad para que todo funcione correctamente.

Es por ello, que una aplicación que le permita gestionar de manera eficiente el stock de los productos (no haya en exceso ni falta), le permita realizar pedidos de productos de manera automática y que además, gestione el inventario de manera que se pueda observar en tiempo real qué productos hay, podría solucionar muchos de los problemas a los que se tendría que enfrentar dicho usuario.

  

## Motivación

La idea del proyecto está basada en resolver los principales problemas a los que se puede enfrentar un gestor de almacén:

- En un almacén se quiere evitar bajo cualquier concepto perder productos porque su fecha de consumo preferente pase.

- La capacidad de almacenamiento es finita, por lo que no se pueden pedir exceso de productos

- Por otro lado, hay productos que se venden normalmente y cuyo pedido se repite cada cierto tiempo, por lo que sería muy útil que se pidieran solos

- Además, sería muy útil recibir la estadística del historial de ventas de cada producto para estimar el tiempo para la próxima compra y la cantidad necesaria

  
## Guía de instalación y uso
En primer lugar habrá que descargar el proyecto desde este repositorio, usando la orden:
  - git clone git@github.com:eantoniocalo18/IV

Una vez descargado el proyecto y todas sus dependencias, podremos realizar las siguientes acciones:

- invoke test : Permitirá ejecutar los test de la aplicación
- invoke check : Comprobará la sintaxis de los archivos de la aplicación
   
### Testeo de clase principal
Para el testeo del código de la clase principal, se usará pytest.
La ejecución de estos test recaerá principalmente sobre la clase Inventario, que a su vez tendrá una serie de productos almacenados.
Para llevar a cabo la ejecución,nos situaremos en la carpeta principal del proyecto y escribiremos:
  - invoke test 

Con esto, pytest buscará entre los diferentes archivos aquellos que empiecen por 'test_', sin embargo, también podríamos indicarle que ejecute un test en concreto o un directorio en el que buscar.
Si queremos ejecutar los test en un entorno aislado, podremos hacerlo ejecutando los siguientes comandos, que crearán y ejecutaran un docker:
  - invoke docker_build
  - invoke docker_run 


Los test implementados corresponden con las siguientes funcionalidades del sistema:

  - Saber cuál es el estado actual del almacén, que es útil saberlo antes de hacer un pedido.
  - Saber si algún producto del almacén tiene bajo stock.
  - Saber si algún producto del almacén tiene mucho stock.


## Documentación

La documentación del proyecto se encuentra en el archivo en [este enlace](https://github.com/eantoniocalo18/IV/tree/main/docs)

 - En el archivo [Issues](https://github.com/eantoniocalo18/IV/docs/ISSUES.md) se encuentra la información relacionada con los tipos de usuario, las historias de usuario y los milestones
 - En el archivo [Eleccion lenguaje](https://github.com/eantoniocalo18/IV/docs/eleccion_lenguaje.md) se encuentra la información relacionada con la elección del lenguaje y el desarrollo de la clase Producto.
 - En el archivo [Eleccion gestores](https://github.com/eantoniocalo18/IV/docs/eleccion_gestores.md) Se ha justificado la elección de los gestores de dependencias y tareas.
 - En el archivo [Dockers](docs.docker.md) Se ha justificado la elección de la imagen Docker que ha servido de base.
