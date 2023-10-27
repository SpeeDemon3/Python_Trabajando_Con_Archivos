import json

def get_stored_username():
    """Obtiene un nombre de usuario almacenado si esta disponible"""
    filename = 'username.json'

    try:
        with open(filename) as f:  # Intentamos abrir el archivo
            username = json.load(f)  # Si existe lo leemos y dentro del bloque else lo saludamos
    except FileNotFoundError:  # Si no existe el archivo probocara un error, lo controlamos
        return None
    else:
        print(f"Welcome back, {username}")

def get_new_username():
    """Solicita un nuevo nombre de usuario"""
    username = input("What's your name?: ")  # Pedimos el nombre
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)  # Lo guardamos
    return username

def greet_user():
    """Saluda y guarda el nombre de un usuario"""
    username = get_stored_username()

    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")


greet_user()