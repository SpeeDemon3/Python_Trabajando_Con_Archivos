# Manejar la excepcion ZeroDivisionError

try:
    number_a = 3
    number_b = 0
    print(number_a / number_b)
except ZeroDivisionError:
    print("You can't divide by zero :-)")

# Ejemplo
# Calculadora de divisiones como ejemplo para poder segir corriendo el programa
# aunque salte una excepcion
print("Give me two numbers, and I'll divide them.")
print("Enter [q] to quit.")

running = True
while running:
    first_number = input("\tFirst number:")
    if first_number == "q":
        running = False

    else:
        second_number = input("\tSecond number:")
        if second_number == "q":
            running = False

        else:
            try:
                answer = int(first_number) / int(second_number)
                print(answer)
            except ZeroDivisionError:
                print("You can't divide by 0.")

### Manejar la Excepcion FileNotFoundError

# Guardo en una variable un archivo no existente
file_not = "file.txt"

try:
    with open(file_not, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"The file {file_not} does not exist.")


### Analizamos un archivo que si existe

tale = 'python_tale.txt'

try:
    with open(tale, encoding="utf-8") as f:
        contents_tale = f.read()
except FileNotFoundError:
    print(f"The file {tale} does not exist.")

# Partimos el texto por palabras con el metodo split()
words = contents_tale.split()
# Obtenemos el numero aproximado de palabras
number_words = len(words)
print(f"The file {tale} has about {number_words} words.")

### TRABAJAR CON MULTIPLES ARCHIVOS

"""Metodo para obtener el numero de palabras que contiene un texto aproximadamente"""
def count_words(file: object) -> object:
    try:
        with open(file, encoding="utf-8") as f:
            contents_file = f.read()
    except FileNotFoundError:
        print(f"The file {file} doesn't exist.")
    else:
        words_list = contents_file.split()
        num_words = len(words)

        print(f"The file {file} has about {num_words} words.")


file_java_tale = "java_tale.txt"
count_words(file_java_tale)

filenames = [file_not, "python_tale.txt", "java_tale.txt"]
for filename in filenames:
    count_words(filename)