import functions
import PySimpleGUI as sg
import time

# TealMono, NeonBlue1

sg.theme("TealMono")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input = sg.InputText(tooltip="Enter the todo: ", key="new_todo")

list = sg.Listbox(values=functions.get_todolist(),
                  key="list_todo", enable_events=True, size=[45, 10])

exit_button = sg.Button("Exit")
add_button = sg.Button("Add", size=(10, 1))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", tooltip="Delete the todo")
edit_button = sg.Button("Edit")

window = sg.Window("Add the to_do",
                   layout=[[clock],
                           [label],
                           [input, add_button],
                           [list, edit_button, complete_button],
                           [exit_button]],
                   font=["Helvitica", 14])

while True:
    event, values = window.read(timeout=999)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            try:
                todo_to_edit = values["list_todo"][0]
                new_todo = values["new_todo"]

                todo_list = functions.get_todolist()
                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo
                functions.write_todolist(todo_list)
                window["list_todo"].update(values=todo_list)
            except IndexError:
                sg.popup( "Select an item first sir!", title="SIRRR")

        case "Complete":
            try:
                todo_to_complete = values["list_todo"][0]
                todo_list = functions.get_todolist()
                todo_list.remove(todo_to_complete)
                functions.write_todolist(todo_list)
                window["list_todo"].update(values=todo_list)
                window["new_todo"].update(value="")
            except IndexError:
                sg.popup( "Select an item first sir!", title="SIRRR")

        case "list_todo":
            window["new_todo"].update(value=values["list_todo"][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
            # exit()

print("bye bye")
window.close()
