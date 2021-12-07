from invoke import task, run

@task
def check(c):
	'''
	Comprobando la sintaxis del proyecto
	'''
	run("pyflakes src")
	print("No hay fallos")
@task
def test(c):
    '''
    Realiza el test de la version del proyecto
    '''
    print("No hay test disponibles actualmente")
