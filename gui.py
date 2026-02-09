import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input = sg.InputText(tooltip="Enter the todo: ", key="new_todo",
                     background_color="light blue")

add_button = sg.Button("Add")

list = sg.Listbox(background_color="pink",
                  values=functions.get_todolist(),
                  key="list_todo", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

window = sg.Window("Add the to_do",
                   layout=[[label], [input], [add_button],
                           [list, edit_button]],
                   font=["Helvitica", 14])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todolist()
            new_todo = values["new_todo"] + "\n"
            todo_list.append(new_todo)
            functions.write_todolist(todo_list)
            window["list_todo"].update(values=todo_list)
        case "Edit":
            todo_to_edit = values["list_todo"][0]
            new_todo = values["new_todo"]


            todo_list = functions.get_todolist()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.write_todolist(todo_list)
            window["list_todo"].update(values=todo_list)
        case "list_todo":
            window["new_todo"].update(value=values["list_todo"][0])
        case sg.WIN_CLOSED:
            break
            # exit()

print("bye bye")
window.close()
