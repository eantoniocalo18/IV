# Marco de tests

## Requisitos

- Salida legible, fácil de entender
- Permita el uso de Fixtures
- Mantenimiento activo de los desarrolladores
- Permite el uso de diferentes librerías de aserciones.

## Búsqueda de alternativas

### Pytest
- La salida que ofrece es limpia y fácilmente entendible ✓
- fixture es una orden de pytest ✓
- Los issues suelen contestarse rápidamente y además incluyendo nuevos commits ✓
- Permite el uso de diferentes librerías de aserciones ✓

### UNITTEST
- Permite el uso de fixtures _fixtures_ ✓
- Su salida es clara aunque no muy descriptiva 1/2 
- Actualmente cuenta con más de 1,5k PRs abiertos, muchos de ellos reportando bugs sin resolver X
- Permite el uso de diferentes librerías de aserciones ✓

### NOSE Y NOSE 2
El lema de NOSE es "NOSE extiende unittest para facilitar las pruebas".
Actualmente NOSE está en desuso y NOSE 2 también se ha basado en Pytest para su desarrollo.
- Permite el uso de fixtures. ✓
- Salida similar a Unittest 1/2
- El mantenimiento de NOSE es nulo, pues está declarado en desuso. X
- Mientras que el de NOSE2 también está algo olvidado pues tiene issues declarados desde el 2018 y sin respuesta. X
- Permite el uso de diferentes librerías de aserciones ✓

## Elección
Como se ha podido comprobar, según los requisitos establecidos las valoraciones han quedado:
- Pytest 4/4
- Unittest 2,5/4
- Nose y Nose2 2,5/4
Por lo tanto se ha elegido Pytest 


# Librería de aserciones
## Requisitos
- Sintaxis sencilla
- Lanzamiento de excepciones
- Aserciones implementadas
- Salida descriptiva

## Búsqueda de alternativas

### Assertpy
- Sintaxis sencilla buscando acercarse al lenguaje natural
- No permite el lanzamiento de excepciones, su gran desventaja
- Permite realizar comprobaciones de forma sencilla sobre objetos más complejos como datetime, ficheros u objetos compuestos
- La salida es similar a __assert__

### Grappa
- Ofrece una sintaxis un poco más ligera a Assertpy
- Ofrece una salida muy extensa, permitiendo mostrar el código
- Tiene menos aserciones que Assertpy
- Permite el lanzamiento de excepciones

### Unittest
Unittest también puede ser usado como una librería de aserciones, usándolas bajo una clase 'test' .

### Hypotesis 
- Ofrece una sintaxis sencilla
- La salida es bastante descriptiva
- Ofrece un gran número de aserciones
- Permite el lanzamiento de excepciones

## Elección
 Comprobando las opciones que se tienen, se descarta en primer lugar Unittest puesto que no veo necesario ni fácil de usar de manera conjunta el mismo software para ambas cosas.
 Por otro lado, la principal diferencia entre Grappa y Assertpy es que éste ofrece un mayor numero de aserciones, puesto que descartamos Grappa.
 
 Por último, entre Assertpy y Hypotesis he elegido Hypotesis en una primera instancia y tras realizar varias pruebas de toma de contacto he decidido que no es tan sencilla de usar y las funcionalidades específicas que presenta no resultan útiles para este proyecto. 
 Por lo tanto se ha elegido Assertpy como librería de aserciones.



