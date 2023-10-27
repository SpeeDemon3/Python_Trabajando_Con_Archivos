import json

### Programa para cargar el nombre de usuario si se ha guardado previamente
### Si no existe, solicita el nombre de usuario y lo guarda

filename = 'username.json'

try:
    with open(filename) as f: # Intentamos abrir el archivo
        username = json.load(f) # Si existe lo leemos y dentro del bloque else lo saludamos
except FileNotFoundError: # Si no existe el archivo probocara un error, lo controlamos
    username = input("What's your name?: ") # Pedimos el nombre
    with open(filename, 'w') as f:
        json.dump(username, f) # Lo guardamos
        print(f"We'll remember you when you come back, {username}")
else:
    print(f"Welcome back, {username}")