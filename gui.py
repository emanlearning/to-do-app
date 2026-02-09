import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input = sg.InputText(tooltip="Enter the todo: ", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Add the to_do",
                   layout=[[label], [input], [add_button]],
                   font=["Helvitica", 13])

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todo_list = functions.get_todolist()
            new_todo = value["todo"] + "\n"
            todo_list.append(new_todo)
            functions.write_todolist(todo_list)
        case sg.WIN_CLOSED:
            break


window.close()