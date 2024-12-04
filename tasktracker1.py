import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)
        on_process_listbox.delete(0, tk.END)

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"✓ {task}")
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to move a task to "On Process"
def move_to_process():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        on_process_listbox.insert(tk.END, task)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to toggle window visibility with Alt + H
def toggle_visibility(event=None):
    if root.state() == "normal":
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window

# Main window
root = tk.Tk()
root.title("TaskTracker 1.0")
root.geometry("600x400")  # Increased size for better usability

# Bind Alt + H to toggle visibility
root.bind("<Alt-h>", toggle_visibility)

# Bind Enter key to the add_task function
root.bind("<Return>", lambda event: add_task())

# Task entry field
task_entry = tk.Entry(root, width=60)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Selected Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

mark_done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done)
mark_done_button.grid(row=0, column=2, padx=5)

move_process_button = tk.Button(button_frame, text="Move to 'On Process'", command=move_to_process)
move_process_button.grid(row=0, column=3, padx=5)

clear_button = tk.Button(button_frame, text="Clear All Tasks", command=clear_tasks)
clear_button.grid(row=0, column=4, padx=5)

# Task list section
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# "To-Do" Listbox
task_listbox = tk.Listbox(list_frame, width=50, height=10)
task_listbox.grid(row=0, column=0, padx=10)

# "On Process" Listbox
on_process_listbox = tk.Listbox(list_frame, width=50, height=10)
on_process_listbox.grid(row=0, column=1, padx=10)

# Labels for each section
todo_label = tk.Label(root, text="To-Do List")
todo_label.pack(side=tk.LEFT, padx=120)

process_label = tk.Label(root, text="On Process")
process_label.pack(side=tk.RIGHT, padx=120)

# Run the application
root.mainloop()
