
while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip() # remove the whitespace from the user input.

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show':
            for index, item in enumerate(todos): # iterate over the existing todos lists.
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to Edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            # todos[number] = new_todo
            todos.__setitem__(number, new_todo)
        case 'complete':
            number = int(input("Index of the todo to Complete: "))
            todos.pop(number - 1)
        case 'exit':
            break # break statement is executed and the while loop terminates.
        case _:
            print("Hey, you entered an unknown command.")

print("BYE!")
