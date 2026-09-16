def greet(name="Avoy"):
    print(f"Hello {name}")

user_input = input("Enter name: ")

if user_input.strip() == "":
    greet()
else:
    greet(user_input)