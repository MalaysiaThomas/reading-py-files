with open("TODO.txt", "r") as file:
    todo_list = file.readlines()

def display_todo_list():
    print("Malaysia's To-Do List:\n")
    for item in todo_list:
        item = item.rstrip()
        print(f"→ {item}")

display_todo_list()