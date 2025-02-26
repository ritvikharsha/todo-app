import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")
clock = sg.Text('', key = "clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key = "todo" )
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My TO-DO App',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font = ("Monospace", 12))
while True:
    event, values = window.read(timeout = 500)
    window["clock"].update(value = time.strftime("%d %b-%Y  %H:%M:%S"))
    """
    (event) -#here events holds the keys of list box , input box
    (values) -#here values holds the current value entered or selected by the user in the list box
              values holds dictonary 
    """
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            #widows can be accessed with window["widgets_Key"] and values can be updated by update()

        case "Edit":
            try:
                todo_to_edit = values['todos'][0] #here 0 is used to extract the sting from the dictonary(values)
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("please select the item first..!", font = ("Monospace",13))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '') #value bcz it contain (1)single value
            except IndexError:
                sg.popup("please select the item first..!", font = ("Monospace",13))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value = values['todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()
