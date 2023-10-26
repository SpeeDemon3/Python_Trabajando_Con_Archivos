# Manejar la excepcion ZeroDivisionError

try:
    number_a = 3
    number_b = 0
    print(number_a / number_b)
except ZeroDivisionError:
    print("You can't divide by zero :-)")