import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    fresh_todo = st.session_state["new_todo"]
    todos.append(fresh_todo + "\n")
    functions.write_todos(todos)


# title for the app
st.title("Minimalist todo app")

# todos list for the app
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# add new todos in input box
st.text_input(label="", placeholder="add new todo", on_change=add_todo,
              key="new_todo")










