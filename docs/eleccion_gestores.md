# Gestor de tareas
Para elegir un gestor de tareas que se ajuste a las necesidades de este proyecto se han tenido en cuenta los siguientes requisitos:
- Sintaxis sencilla
- Mantenimiento continuo
- Facilidad de uso
- Popularidad

## Explicación
Lo principal para un desarrollador es que el software que utilice le facilite todo, es por ello que un requisito con mucho valor que su uso sea fácil, sin tener que configurar en exceso y con un uso casi trivial.
Por otro lado, otro requisito importante es el mantenimiento, puesto que no podemos basar nuestro proyecto en un task runner que no se haya actualizado en los últimos años o que directamente esté abandonado, puesto que ante un fallo del programa no tenemos la seguridad de que los desarrolladores del mismo vayan a tratar de solucionarlo.
Por último, la popularidad de un software nos indica dos cosas: Realiza bien su función y tiene una comunidad de personas que lo usan. Esto nos garantiza que al elegir un task runner muy popular encontraremos muchos sitios web donde podremos exponer problemas, ver problemas de gente e incluso en el caso de que se reporten fallos es posible que sean los mismos usuarios del software quienes los solucionen.

# Gestor de dependencias
Se han barajado varias alternativas cuyas principales ventajas/desventajas son:
  - Easy Install: Es incluido setuptools que permite descargar, construir, instalar y administrar paquetes de Python automáticamente. Fue lanzado en 2004 y está obsoleto.
  - Pip: Ofrece los mismos servicios que el anterior pero además permite desinstalar paquetes y sobreescribir dependencias.
  - Poetry: Un gestor de dependencias y un empaquetador de librerías python. Con respecto a los demás, permite el control de versiones y también realizar actualizaciones del software ya instalado.


