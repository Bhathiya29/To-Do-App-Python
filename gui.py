import functions_of_todo
import PySimpleGUI

label = PySimpleGUI.Text('Type in a To-Do')
input_box = PySimpleGUI.InputText(tooltip='Enter To-Do', key='todo')
add_button = PySimpleGUI.Button('Add')

window = PySimpleGUI.Window("My To-Do App",
                            layout=[[label, input_box, add_button]],
                            font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo=functions_of_todo.getTodos()
            todo.append(values['todo']+'\n') #todo is the key to retrieve its value
            functions_of_todo.writeTodos(todo)

        case PySimpleGUI.WIN_CLOSED:
            break





window.close()
