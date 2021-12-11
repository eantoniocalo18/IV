# Gestor de tareas
Para elegir un gestor de tareas se han tenido en cuenta los siguientes requisitos:
- Sintaxis sencilla
- Mantenimiento continuo
- Popularidad
- Específico para el lenguaje de programación escogido
## Explicación
Una de las principales razones por las que un desarrollador elige un software o otro es su facilidad de uso, es por ello que un requisito con mucho valor que su uso sea fácil, sin tener que configurar en exceso y con un uso casi trivial.
Por otro lado, otro requisito importante es el mantenimiento, puesto que no podemos basar nuestro proyecto en un task runner que no se haya actualizado en los últimos años o que directamente esté abandonado, puesto que ante un fallo del programa no tenemos la seguridad de que los desarrolladores del mismo vayan a tratar de solucionarlo.
Por último, la popularidad de un software nos indica dos cosas: Realiza bien su función y tiene una comunidad de personas que lo usan. Esto nos garantiza que al elegir un task runner muy popular encontraremos muchos sitios web donde podremos exponer problemas, ver problemas de gente e incluso en el caso de que se reporten fallos es posible que sean los mismos usuarios del software quienes los solucionen.

## Alternativas
Las diferentes alternativas que se contemplan son las siguientes:
- make: Permite configurar en un solo archivo Makefile todas las acciones, aunque no es un task runner como tal se puede usar 
  - Las ventajas que presenta make con respecto a los requisitos de elección es que sigue actualizándose actualmente y su sintáxis no es especialmente compleja
  - Las desventajas es que no es un task runner como tal por lo que su popularidad como task runner no es mucha. Además, su uso no es específico de Python pues es un comando de Linux.
- invoke: Permite configurar las tareas en un archivo task.py.  No tiene dependencias
  - Las ventajas es que está escrito en Python, por lo que la sintaxis es muy conocida y está en mantenimiento continuo. Es específico para proyectos Python
  - Es el más popular para proyectos Python.
- poethepoet: Es un software específico de python. Tiene algunas dependencias.
  - Entre las ventajas de poethepoet está su mantenimiento, que contestan rápidamente a los issues que plantean los usuarios. Además, es específico para proyectos Python
  - Las desventajas son que tiene otras dependencias y que su configuración es algo más compleja que los demás taskrunner contemplados.
- DoIt: Es un software que está en mantenimiento actualmente y es específico de python.
  - Sus ventajas es que es específico para proyectos Python y está en mantenimiento continuo
  - Sin embargo, requiere de otras dependencias.

Por lo tanto, basando la decisión en los requisitos y viendo las principales ventajas y desventajas que muestran cada uno de ellos se ha optado por usar Invoke, principalmente por su popularidad y su facilidad de uso. 


