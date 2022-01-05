#Integración continua

## Definición de tareas

Las tareas que se van a llevar a cabo y para las cuales se requiere de un sistema de integración continua son las siguientes:
- Ejecutar pruebas de código con diferentes versiones del lenguaje de programación utilizado.
- Automatizar la ejecución de los test del código para que se ejecuten cada vez que se hace un PR. Siguiendo la filosofía de 'código no probado, es código roto'. 

## Definición de requisitos

Los requisitos que nos servirán para valorar positiva o negativamente una herramienta de integración continua serán los siguientes:
- Soporte para Github
- Versión de prueba / servicio gratuito
- Soporte para Docker
- Administración en la nube


## Alternativas encontradas

- [AWS Code Build](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) : 
    - Cuenta con herramientas de compilación como Apache Maven, Gradle y además también puede usar sus propiar herramientas.
    - Totalmente administrado en la nube, no existe la necesidad de configurar, actualizar y administrar los servidores de compilación
    - No permite una conexión con Github ni Docker, además de que su servicio gratuito es de 100 minutos.
AWS Code Build no cumple con todos los requisitos que habíamos definido anteriormente, por lo tanto se descarta como posible opción.

- [Circle CI](https://circleci.com/docs/) : 
    - Permite probar nuestro código con diferentes versiones de Python.
    - Está administrado en la nube.
    - Tiene soporte para Github y Docker.
    - Su prueba gratuita permite recargar los créditos (forma de representar los minutos y su coste) al inicio de cada mes.

Circle CI cumple con todos los requisitos que habíamos definido, por lo tanto es una buena opción para integrar en nuestro proyecto.

- [Travis CI](https://travis-ci.org/) : 
    - Administración basada en la nube.
    - Cuenta con una matriz de versiones que permite probar diferentes versiones de Python (entre otros muchos lenguajes).
    - Además, se integra con Docker y Github.
    - Su servicio gratuito está basado en una serie de créditos iniciales que no se recargarán, por lo tanto tendríamos que pagar una vez se nos acaben.

Las funcionalidades y características de Travis CI son las que necesita nuestro proyecto, sin embargo su periodo de prueba obliga a descartarlo puesto que una vez terminado el periodo de prueba no vuelves a contar con minutos gratis y posiblemente este periodo de prueba no sea suficiente para llevar a cabo el proyecto de manera totalmente gratuita.

- [GitHub Actions] (https://github.com/features/actions) :
    - Administración basada en la nube.
    - Cuenta con una matriz de versiones que permite probar diferentes versiones de Python (entre otros muchos lenguajes).
    - Al igual que Circle CI, da una serie de créditos que se recargan al principio de cada mes.
    - Soporte para Docker y GitHub.

Esta herramienta también cumple con todos los requisitos que se han definido, por lo tanto es una opción a contemplar en la decisión final.

## Elección final

Tras definir los requisitos y comprobar cuáles de las herramientas los cumplen, tenemos dos herramientas que cumplen los requisitos:
    - Circle CI
    - GitHub Actions

Ambas herramientas podrían ser utilizadas para el desarrollo del proyecto, por lo tanto, dado que no tenemos créditos ilimitados en ninguna de ellas, vamos a usar ambas.
    - Github Actions ya ha sido utilizada anteriormente en este proyecto, por lo que ya estoy familiarizado con ella. Por lo tanto, se va a usar para la ejecución automática de los test cada vez que se realice un PR. Para el desarrollo, se usará la [documentación oficial](https://github.com/docker/build-push-action) que proporciona github para la creación y subida de contenedores.

    - Por otro lado, [Circle CI](https://github.com/circleci/circleci-docs) será usada para la ejecución del proyecto sobre las diferentes versiones de Python. Se usará la versión 2.1 ya que es la más actual y se comprobará para qué versiones de Python el proyecto funciona correctamente. 

# Versiones del lenguaje

Este proyecto ha sido desarrollado en Python, usando la version 3.9 y [estas herramientas](https://github.com/eantoniocalo18/IV/blob/main/pyproject.toml)
Sin embargo, tenemos que proporcionar al usuario final la mayor información posible sobre nuestro proyecto, incluyendo en qué versiones de Python funciona correctamente el proyecto.
Siguiendo la [guía del desarrollador de Python](https://devguide.python.org/#status-of-python-branches) podemos ver que las versiones 3.7 y 3.8 ya no lanzarán más archivos binarios solo correciones de seguridad, sin embargo, su ciclo de vida finalizará en junio 2023 y 2024 respectivamente. Por lo tanto, estas versiones deben ser testeadas ya que siguen siendo usadas por la comunidad y en mantenimiento.
Por otra parte, las versiones 3.9 y 3.10 se consideran estables y siguen en mantenimiento activo y está previsto su fin de vida en 2026 y 2027 respectivamente. Estas versiones siguen en mantenimiento y se aceptan correciones de seguridad y de errores, además son las más usadas desde el 2020 [info](https://www.mclibre.org/consultar/python/otros/historia.html), por lo que también testearemos estas versiones.