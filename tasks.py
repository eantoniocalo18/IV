from invoke import task, run

@task
def check(c):
	'''
	Comprobando la sintaxis del proyecto
	'''
	run("python -m compileall src/* ")
	print("No hay fallos")
@task
def test(c):
    '''
    Realiza el test de la version del proyecto
    '''
    run ('pytest')
    
def docker_build(c):
    '''
    Crea la imagen del docker
    '''
    run ('docker build -t eantoniocalo18/iv .')

def docker_run(c):
    '''
    Ejecuta el docker
    '''
    run ('sudo docker run -t -v `pwd`:/app/test eantoniocalo18/iv
')
