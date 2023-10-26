# Escribir y crear si no es existe un archivo

# Creamos una variable con el nombre del archivo
file_name = 'writer_message.txt'

# Dentro de open('archivo_para_escribir' , 'w') indicamos el archivo y que queremos escribir en el
with open(file_name, 'w') as file_object:
    file_object.write("I love Python!!!") # Dentro del metodo write() introducimos el contenido que queremos escribir en el archivo

# Leemos el archivo
with open(file_name, 'r') as file_object:
    print(file_object.readlines())