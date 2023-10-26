import json
### Guardar datos en un archivo JSON
numbers = [2, 3, 4, 5, 6, 7, 8]

filename = 'numbers.json'

with open(filename, "w") as f:
    json.dump(numbers, f) # Utilizamos dump() para guardar los numeros de la lista en formato JSON

print(filename)