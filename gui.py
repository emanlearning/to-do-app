import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input = sg.InputText(tooltip="Enter the todo: ")
add_button = sg.Button("Add")

window = sg.Window("Add the to_do", layout=[[label], [input], [add_button]])
window.read()
print("hello")
window.close()