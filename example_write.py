
ask_name = input("What's your name?")

with open("guest.txt","w") as file_object:
    file_object.write(ask_name)

print("-Guest Book-")
count_guest = 1
while count_guest < 6:
    new_guest = input("What's your name: ")
    print(f"Welcome {new_guest}")
    with open("guest_book.txt", "a") as file_object:
        file_object.write(f"{count_guest}: {new_guest}\n")

    count_guest += 1