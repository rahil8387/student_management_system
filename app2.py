import tkinter as tk
from tkinter import messagebox
from students import Student 
from storage import load_data, save_data 
import pickle 

def add_data():
    """Reads input from the GUI, creates a Student, and saves it."""
    name = name_entry.get()
    rollno = roll_entry.get()
    marks_str = marks_entry.get()

    # Basic validation
    if not name or not rollno or not marks_str:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        marks = int(marks_str)
    except ValueError:
        messagebox.showerror("Type Error", "Marks must be an integer number!")
        return

    # Save data
    try:
        s1 = Student(name, rollno, marks)
        save_data(s1)
        messagebox.showinfo("Success", f"Student '{name}' added successfully!")
        
        # Clear the input fields after successful save
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        marks_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data:\n{e}")

def display_data():
    """Loads data and displays it in the text box."""
    try:
        data = load_data()
        
        # Clear the text box before inserting new data
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, str(data))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data:\n{e}")

# --- GUI Setup ---
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("400x450")
    root.config(padx=20, pady=20)

    # --- Input Fields ---
    tk.Label(root, text="Student Name:").grid(row=0, column=0, sticky="e", pady=5)
    name_entry = tk.Entry(root, width=25)
    name_entry.grid(row=0, column=1, pady=5, padx=10)

    tk.Label(root, text="Roll Number:").grid(row=1, column=0, sticky="e", pady=5)
    roll_entry = tk.Entry(root, width=25)
    roll_entry.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(root, text="Marks:").grid(row=2, column=0, sticky="e", pady=5)
    marks_entry = tk.Entry(root, width=25)
    marks_entry.grid(row=2, column=1, pady=5, padx=10)

    # --- Buttons ---
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, columnspan=2, pady=20)

    tk.Button(button_frame, text="Add Data", command=add_data, width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Load Data", command=display_data, width=10).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Exit", command=root.destroy, width=10).grid(row=0, column=2, padx=5)

    # --- Output Display ---
    tk.Label(root, text="Loaded Data:").grid(row=4, column=0, columnspan=2, sticky="w")
    output_box = tk.Text(root, height=10, width=40)
    output_box.grid(row=5, column=0, columnspan=2, pady=5)

    # Start the GUI event loop
    root.mainloop()