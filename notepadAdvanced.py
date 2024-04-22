import tkinter as tk
from tkinter import filedialog, simpledialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text.delete('1.0', tk.END)
        with open(file_path, 'r') as file:
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

def close_app():
    root.quit()

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def paste_text():
    text.insert(tk.INSERT, text.clipboard_get())

def cut_text():
    copy_text()
    text.delete("sel.first", "sel.last")

def clear_text():
    text.delete('1.0', tk.END)

def find_text():
    find_string = simpledialog.askstring('Find', 'Enter text')
    text.tag_remove('found', '1.0', tk.END)
    if find_string:
        idx = '1.0'
        while True:
            idx = text.search(find_string, idx, nocase=1, stopindex=tk.END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(find_string))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red')

def undo_text():
    try:
        text.edit_undo()
    except tk.TclError:
        pass

def redo_text():
    try:
        text.edit_redo()
    except tk.TclError:
        pass

root = tk.Tk()
text = tk.Text(root, undo=True)
text.pack()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Close", command=close_app)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Clear", command=clear_text)
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)

root.mainloop()
