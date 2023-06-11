import streamlit as st
import functions_of_todo as func

todos = func.getTodos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    func.writeTodos(todos)


# App Script Starts ------------------

st.title('My ToDo App')
st.subheader('This is my to do app')
st.text('This app is to increase productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

    # Adding todo items to the list and calling the responsible function
user_input = st.text_input(label='', placeholder='Enter a to-do',
                           on_change=add_todo, key='new_todo') + '\n'

# print(todos) Testing purpose codeline

# st.session_state Testing purpose codeline

# App Script Ends --------------------
