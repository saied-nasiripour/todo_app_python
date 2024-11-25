
todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip() # remove the whitespace from the user input.

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos: # iterate over the existing todos lists.
                print(str(todos.index(item) + 1) + ". " + item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break # break statement is executed and the while loop terminates.
        case _:
            print("Hey, you entered an unknown command.")

print("BYE!")
