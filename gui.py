import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window('My TO-DO App', layout=[[label],[input_box,add_button]])
window.read()
print("Hello")
window.close()
