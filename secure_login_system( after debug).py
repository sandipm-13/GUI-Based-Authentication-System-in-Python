import tkinter as tk
from tkinter import messagebox
import os
import re

# Constants
MAX_LOGIN_ATTEMPTS = 3
MIN_USERNAME_LENGTH = 4
MIN_PASSWORD_LENGTH = 6

users = {}
login_attempts = {}

# Load users from file
def load_users():
    if not os.path.exists("users.txt"):
        return {}
    with open("users.txt", "r") as f:
        lines = f.readlines()
        data = {}
        for line in lines:
            line = line.strip()
            if ":" in line:
                uname, pwd = line.split(":", 1)
                data[uname] = pwd
        return data

# Save users to file (overwrites safely)
def save_users(users_dict):
    with open("users.txt", "w") as f:
        for uname, pwd in users_dict.items():
            f.write(f"{uname}:{pwd}\n")

# Input validation
def is_valid(text):
    return re.match(r"^[A-Za-z0-9_]+$", text) and ":" not in text

# Register function
def register_user():
    username = entry_reg_user.get().strip()
    password = entry_reg_pass.get().strip()
    confirm = entry_reg_confirm.get().strip()

    if not username or not password or not confirm:
        messagebox.showerror("Error", "All fields are required.")
        return

    if len(username) < MIN_USERNAME_LENGTH or len(password) < MIN_PASSWORD_LENGTH:
        messagebox.showerror("Error", f"Username must be at least {MIN_USERNAME_LENGTH} characters and password {MIN_PASSWORD_LENGTH}.")
        return

    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    if not is_valid(username) or not is_valid(password):
        messagebox.showerror("Error", "Invalid characters. Use only letters, digits, and underscore. ':' is not allowed.")
        return

    if username in users:
        messagebox.showerror("Error", "Username already exists.")
        return

    users[username] = password
    save_users(users)
    messagebox.showinfo("Success", "Registration successful.")
    register_window.destroy()

# Show register window
def show_register():
    global register_window, entry_reg_user, entry_reg_pass, entry_reg_confirm
    register_window = tk.Toplevel(app)
    register_window.title("Register")
    register_window.geometry("300x260")
    register_window.config(bg="#e0f7fa")

    tk.Label(register_window, text="Username", bg="#e0f7fa").pack(pady=5)
    entry_reg_user = tk.Entry(register_window)
    entry_reg_user.pack()

    tk.Label(register_window, text="Password", bg="#e0f7fa").pack(pady=5)
    entry_reg_pass = tk.Entry(register_window, show="*")
    entry_reg_pass.pack()

    tk.Label(register_window, text="Confirm Password", bg="#e0f7fa").pack(pady=5)
    entry_reg_confirm = tk.Entry(register_window, show="*")
    entry_reg_confirm.pack()

    tk.Button(register_window, text="Register", command=register_user, bg="#00796b", fg="white").pack(pady=10)

# Login function
def login_user():
    global login_attempts
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    if username not in users:
        messagebox.showerror("Login Failed", "Username not found.")
        return

    if username not in login_attempts:
        login_attempts[username] = 0

    if users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        entry_user.delete(0, tk.END)
        entry_pass.delete(0, tk.END)
        login_attempts[username] = 0
    else:
        login_attempts[username] += 1
        if login_attempts[username] >= MAX_LOGIN_ATTEMPTS:
            messagebox.showerror("Blocked", "Too many failed attempts. Exiting.")
            app.quit()
        else:
            messagebox.showerror("Login Failed", f"Wrong password. Attempt {login_attempts[username]}/{MAX_LOGIN_ATTEMPTS}")

# Exit app
def exit_app():
    app.destroy()

# Main GUI
app = tk.Tk()
app.title("Secure Login System")
app.geometry("340x280")
app.config(bg="#ffffff")

users = load_users()

tk.Label(app, text="Login System", font=("Arial", 16), bg="#ffffff", fg="#00796b").pack(pady=10)

tk.Label(app, text="Username", bg="#ffffff").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Password", bg="#ffffff").pack()
entry_pass = tk.Entry(app, show="*")
entry_pass.pack()

frame = tk.Frame(app, bg="#ffffff")
tk.Button(frame, text="Login", width=12, bg="#4caf50", fg="white", command=login_user).pack(side="left", padx=10)
tk.Button(frame, text="Register", width=12, bg="#004d40", fg="white", command=show_register).pack(side="left")
frame.pack(pady=15)

tk.Button(app, text="Exit", width=12, bg="#f44336", fg="white", command=exit_app).pack()

app.mainloop()
