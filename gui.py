import functions_of_todo
import PySimpleGUI

label = PySimpleGUI.Text('Type in a To-Do')
input_box = PySimpleGUI.InputText(tooltip='Enter To-Do',
                                  key='todos',
                                  enable_events=True,
                                  size=[45,1000])
edit_button=PySimpleGUI.Button('Edit')
add_button = PySimpleGUI.Button('Add')
listBox=PySimpleGUI.Listbox(values=functions_of_todo.getTodos(),key='todo')

layout=[[label], [input_box, add_button], [listBox, edit_button]]

window = PySimpleGUI.Window("My To-Do App",
                            layout=layout,
                            font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo=functions_of_todo.getTodos()
            todo.append(values['todo']) #todo is the key to retrieve its value
            functions_of_todo.writeTodos(todo)
    
        case 'Edit':
            todo_to_edit=values['todo'][0]
            new_todo=values['todos']+'\n'

            todos=functions_of_todo.getTodos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions_of_todo.writeTodos(todos)
            #window['todos'].update(values='todo')

            

        case PySimpleGUI.WIN_CLOSED:
            break





window.close()
