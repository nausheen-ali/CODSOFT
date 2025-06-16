import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]
        if not task.startswith("[Done] "):
            tasks[selected] = "[Done] " + task
            update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, width=25, font=('Arial', 14))
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, font=('Arial', 14), width=35, height=15, selectbackground="gray")
listbox.pack(pady=10)

done_button = tk.Button(root, text="Mark as Done", command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
