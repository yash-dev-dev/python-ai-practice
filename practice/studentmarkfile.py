with open("studentlist.txt", "w") as file:
    for i in range(3):
        name = input(f"Enter name of student {i+1}: ")
        marks = input(f"Enter marks of student {i+1}: ")
        file.write(f"{name}: {marks}\n")

with open("studentlist.txt", "r") as file:
    print(file.read())