### Leer un archivo JSON
import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f) # Utizando load() cargamos la informacion almacenada en 'numbers.json' y la guardamos en una variable

print(numbers)