import csv

# Función que leerá los datos de un fichero CSV y los pasará a un diccionario de productos

def from_CSV(path):
    with open('data.txt', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file) 
        diccionario= {rows[0]:rows[1] for rows in csv_reader}
    return diccionario
    
    

