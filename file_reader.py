### Este programa habre el archivo, lo lee e imprime el contenido

# Pasamos a la funcion open('el archivo que queremos abrir') y nos devuelve un objeto que representa el archivo
# y se asigna al objeto file_object
# with cierra el programa cuando ya no hace falta acceder a el
with open('pi_digits.txt') as file_object:
    contents = file_object.read()   # Utilizando el metodo read() guardamos el contenido en una cadena de texto
print(contents.rstrip())    # Eliminanos espacios en blanco a la derecha