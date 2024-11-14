from unittest import case

todos = []

while True:
    user_action = input("Type add or Show, exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("BYE!")
