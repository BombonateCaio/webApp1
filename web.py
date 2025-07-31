import streamlit as st
import functions

# Load existing todos
todos = functions.get_todos()

# Initialize completed tasks in session state
if "completed" not in st.session_state:
    st.session_state.completed = []

def add_todo():
    todo = st.session_state["new_todo"].strip() + '\n'
    if todo and todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

# UI - Title
st.title("My Todo List App")
st.subheader("This app helps you list your day-to-day tasks")

# Todo list with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)
    if checkbox:
        # Mark as completed
        st.session_state.completed.append(todo.strip())
        # Remove from main list
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Input to add a new task
st.text_input(label="", placeholder="Enter a new task",
              on_change=add_todo, key="new_todo")

# --- Sidebar with completed tasks ---
with st.sidebar:
    st.header("Completed Tasks")
    if st.session_state.completed:
        for done in st.session_state.completed:
            st.write(f"✔️ {done}")
        if st.button("Clear Completed"):
            st.session_state.completed.clear()
    else:
        st.write("No completed tasks yet.")
