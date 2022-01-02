#Integración continua

## Definición de requisitos

Los requisitos que nos servirán para valorar positiva o negativamente una herramienta de integración continua serán los siguientes:
- Lenguajes soportados (versiones de Python)
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

Las funcionalidades y características de Travis CI son las que necesita nuestro proyecto, sin embargo su periodo de prueba obliga a descartarlo puesto que estamos buscando una herramienta que nos permita llevar a cabo el proyecto de manera gratuita.

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
    - Github Actions ya ha sido utilizada anteriormente en este proyecto, por lo que ya estoy familiarizado con ella. Por lo tanto, se va a usar para la ejecución automática de los test cada vez que se realice un PR.

    - Por otro lado, Circle CI será usada para la ejecución del proyecto sobre las diferentes versiones de Python.

# Versiones del lenguaje

Este proyecto está desarrollado en Python, usando la version 3.9.
Por lo tanto, las versiones en las que tendremos que comprobar si nuestro proyecto funciona serán las posteriores, así como la 3.8, que actualmente también es muy usada por la comunidad.
Sin embargo, no veo la necesidad de comprobar las versiones más antiguas (como la 3.6 que se declarará obsoleta próximamente) dado que poco a poco quedarán obsoletas y no recibirán más actualizaciones, por lo que siempre tenemos que mirar hacia el futuro y asegurarnos de que las nuevas veriones de python serán compatibles con este proyecto.