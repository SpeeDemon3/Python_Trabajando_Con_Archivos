### Trabajar con el contenido de un archivo

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    line = file_object.readline() # El metodo readline() coge cada linea del archivo y la guarda en una lista

