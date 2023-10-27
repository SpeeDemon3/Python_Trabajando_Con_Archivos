### Leer un archivo JSON
import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f) # Utizando load() cargamos la informacion almacenada en 'numbers.json' y la guardamos en una variable

print(numbers)

print('##########################################################')

### Guardar y leer datos generados por un usuario

username = input("What's your name? ")

filename_users = "filename_users.json"

with open(filename_users, 'w') as f:
    json.dump(username, f) # Guardamos el nombre de usuario en el archivo
    print(f"We'll remember you when you come back, {username}")

with open(filename_users) as f:
    user = json.load(f) # Recuperamos el nombre del usuario guardado en el archivo 'filename_users.txt'
    print(f"Welcome back, {user}!!!")