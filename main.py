# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True: #Всеки елемент е True
    user_action = input( "Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # match user_action: #Match case <-- Променлива с многобройни малки променливи
    if user_action.startswith("add"):
        todo = user_action[4:] # \n обединява двата стринга

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos): # това са 2 променливи в фор-цикъла
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            # number = int(input("Number of the todo to edit: ")) Преобразуване на стринг в число
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()


            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:

            print("Your command is not valid")
            continue



    elif user_action.startswith("complete"): # манипулация на листа
           try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was remove from the list."
            print(message)
           except IndexError:
               print("There is no item with that number")
               continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")


print("Bye!")