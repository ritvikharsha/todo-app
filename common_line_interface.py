# from functions import get_todos , write_todos
import functions
import time

now = time.strftime("%d %b-%Y  %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] +'\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] #list comprehensions
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}. {item}')


    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("command is invalid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid")

print("Bye!!..")
