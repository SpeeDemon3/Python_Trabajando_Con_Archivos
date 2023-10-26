### Excepcion ValueError -> Cuando se intenta convertir una letra a valor numerico

value_user = input("Insert the first number:")
value_user_2 = input("Insert the second number:")

def addValues(number1, number2):
    """Metodo para sumar 2 valores controlando la excepcion ValueError"""
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("You have not entered numerical values")
    else:
        print(number1 + number2)


addValues(value_user, value_user_2)

leave = False
while(not leave):
    value_user_3 = input("Insert the first number:")
    value_user_4 = input("Insert the second number:")
    addValues(value_user_3,value_user_4)
    print("Enter [q] to exit.")

    if value_user_3 == "q" or value_user_4 == "q":
        leave = True