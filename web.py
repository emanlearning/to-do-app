import streamlit as st
import functions

todo_list = functions.get_todolist()

st.title("My Todo App")
st.subheader("My Todos")
st.write("Its for practice")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
print("hello nigga")