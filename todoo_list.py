import functions
import time

now = time.strftime("%d %b %Y %H:%M:%S")
print(f"It is {now}")

while True:
    # ask for user prompt and remove white spaces
    ask = input("Type add, show, edit, complete or exit: ")
    ask = ask.strip()

    # action of user prompt
    if ask.startswith("add"):
        task = ask[4:]

        todo_list = functions.get_todolist()

        todo_list.append(task + '\n')

        functions.write_todolist(todolist=todo_list)

    elif ask.startswith("show"):

        todo_list = functions.get_todolist()

        for index, task in enumerate(todo_list):
            task = task.title().strip()
            print(f"{index + 1} - {task}")

    elif ask.startswith("edit"):
        try:
            number = int(ask[5:])
            number -= 1

            todo_list = functions.get_todolist()

            todo = input("Enter the new todo: ")
            todo_list[number] = todo + "\n"

            functions.write_todolist(todo_list)

        except ValueError:
            print("invalid command")
            continue

    elif ask.startswith("complete"):
        try:
            number = int(ask[9:])
            number -= 1

            todo_list = functions.get_todolist()

            todo_to_remove = todo_list[number].strip("\n")

            print(f"the todo '{todo_to_remove}' has been removed")

            todo_list.pop(number)

            functions.write_todolist(todo_list)

        except IndexError:
            print("invalid command")
            continue

    elif ask.startswith("exit"):
        break

    else:
        print("'Invalid Input Try Again'")

print("byeeee!")
