import tkinter as tk
from tkinter import messagebox

# Global list to store book records
library = []

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    isbn = isbn_entry.get()

    if title and author and year and isbn:
        library.append({"Title": title, "Author": author, "Year": year, "ISBN": isbn})
        update_display()
        clear_fields()
        messagebox.showinfo( "Book added successfully!" "Thank You.")
    else:
        messagebox.showwarning("Input Error", "Please verify the input details.")

def delete_book():
    selected = book_listbox.curselection()
    if selected:
        index = selected[0]
        del library[index]
        update_display()
        messagebox.showinfo( "Book deleted successfully!" "Thank You.")
    else:
        messagebox.showwarning("Error", "Choose a book to delete.")

def update_display():
    book_listbox.delete(0, tk.END)
    for idx, book in enumerate(library, 1):
        display_text = f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - ISBN: {book['ISBN']}"
        book_listbox.insert(tk.END, display_text)

def clear_fields():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

# Labels and Entry widgets
tk.Label(root, text="Title").place(x=20, y=20)
title_entry = tk.Entry(root, width=30)
title_entry.place(x=100, y=20)

tk.Label(root, text="Author").place(x=20, y=60)
author_entry = tk.Entry(root, width=30)
author_entry.place(x=100, y=60)

tk.Label(root, text="Year").place(x=20, y=100)
year_entry = tk.Entry(root, width=30)
year_entry.place(x=100, y=100)

tk.Label(root, text="ISBN").place(x=20, y=140)
isbn_entry = tk.Entry(root, width=30)
isbn_entry.place(x=100, y=140)

# Buttons
tk.Button(root, text="Add Book", command=add_book, width=12).place(x=400, y=20)
tk.Button(root, text="Delete Book", command=delete_book, width=12).place(x=400, y=60)
tk.Button(root, text="Exit", command=root.quit, width=12).place(x=400, y=100)

# Listbox to display books
book_listbox = tk.Listbox(root, height=10, width=70)
book_listbox.place(x=20, y=200)

# Start the GUI loop
root.mainloop()
