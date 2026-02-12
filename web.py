import streamlit as st
import functions

todo_list = functions.get_todolist()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todo_list.append(todo)
    functions.write_todolist(todo_list)

st.title("My Todo App")
st.subheader("My Todos")
st.write("Its for practice")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",on_change=add_todo, key="new_todo")

print("hello nigga")
st.session_state