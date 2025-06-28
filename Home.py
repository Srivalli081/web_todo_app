#
import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my first web todo list")
st.write("This helps you to be more productive")
todos_list = functions.get_todos()
#function to update the list and display the new list
def add_todo():
    new_todo = st.session_state["new_todo"]

    if new_todo + '\n' in todos_list:
        st.session_state["msg"] = new_todo + " already exists. " + "Try to add unique todos"

    else:
        todos_list.append(new_todo + '\n')
        functions.write_todos(todos_list)
        st.session_state["new_todo"] = ''
# display all the todos on the screen
# also, delete the selected checkbox
for i, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(i)
        functions.write_todos(todos_list)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")
st.text_input(label="", key="msg")









