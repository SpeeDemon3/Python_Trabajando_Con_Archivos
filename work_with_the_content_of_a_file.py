### Trabajar con el contenido de un archivo

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines() # El metodo readlines() coge cada linea del archivo y la guarda en una lista

pi_str = ''

for line in lines:
    pi_str += line.strip() # Vamos guardando el contenido eliminando espacios

print(pi_str)
print(len(pi_str))

birthday = input("Enter your birthday, in the form MMddYY: ")
if(birthday in pi_str):
    print("Your birthday appears in the digits of pi!!!")
else:
    print("Your birthday doesn't appears in the digits of pi.")