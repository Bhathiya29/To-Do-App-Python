import streamlit as st
import functions_of_todo as func

todos=func.getTodos()

def add_todo():
    todo = st.session_state['new_todo']+'\n'
    todos.append(todo)
    func.writeTodos(todos)


# App Script Starts ------------------

st.title('My ToDo App')
st.subheader('This is my to do app')
st.text('This app is to increase productivity')

for todo in todos:
    st.checkbox(todo)

user_input = st.text_input(label='', placeholder='Enter a to-do',
                           on_change=add_todo,key='new_todo')+'\n'


print(todos)

st.session_state

# App Script Ends --------------------
