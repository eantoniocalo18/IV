# Solución para la instalación de Poetry 
He realizado varias pruebas en distintos sistemas y he visto que al instalar
poetry no siempre se incluye de manera automática la variable de entorno al PATH, por
lo tanto voy a explicarlo brevemente:


--- En Unix ---
- Para saber qué variable $home tenemos 
	echo $HOME
- Para exportar la variable $PATH
	export PATH=$PATH:$HOME/.poetry/bin

--- En Windows ---
Añadir desde la interfaz gráfica a la variable de entorno PATH el siguiente contenido:
	%USERPROFILE%\.poetry\bin
