### Escribir y crear si no es existe un archivo

# Creamos una variable con el nombre del archivo
file_name = 'writer_message.txt'

# Dentro de open('archivo_para_escribir' , 'w') indicamos el archivo y que queremos escribir en el
with open(file_name, 'w') as file_object:
    file_object.write("I love Python!!!") # Dentro del metodo write() introducimos el contenido que queremos escribir en el archivo

# Leemos el archivo
with open(file_name, 'r') as file_object:
    print(file_object.readlines())

print("------------------------------------------")

# Escribir multiples lineas, pasando el parametro 'w' Python sobrescribira el contenido al volver
# a abrir el archivo
with open(file_name, 'w') as file_object:
    file_object.write("New line \n")
    file_object.write("new line \n")

with open(file_name) as file_object:
    print(file_object.readlines())

print("------------------------------------------")


# Escribir multiples lineas, pasando el parametro 'a' Python no sobrescribira el contenido al volver
# a abrir el archivo
with open(file_name, 'a') as file_object:
    file_object.write("More new lines \n")
    file_object.write("More new lines \n")

with open(file_name, "r") as file_object:
    content = file_object.readlines()
    print(content)