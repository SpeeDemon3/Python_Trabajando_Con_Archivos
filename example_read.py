
file = 'learning_python.txt'

with open(file) as file_object:
    print(file_object.read())

print('##############################################')

with open(file) as file_object:
    for line in file_object:
        print(file.strip())

print('##############################################')

with open(file) as file_object:
    list_lines = file_object.readlines()

string_lines = ""

for line in list_lines:
    string_lines += line

print(string_lines)