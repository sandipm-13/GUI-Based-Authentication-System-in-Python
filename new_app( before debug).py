import tkinter as tk
from tkinter import messagebox
import os
import random

# Load users from file safely
def load_users():
    if not os.path.exists("users.txt"):
        return {}
    with open("users.txt", "r") as file:
        lines = file.readlines()
        users_dict = {}
        for line in lines:
            line = line.strip()
            if ":" in line:
                username, password = line.split(":", 1)
                users_dict[username] = password
        return users_dict

# Save a new user to file
def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

users = load_users()
register_attempts = {}  # Track registration attempts per username

# Register user function (called by register window)
def register_user():
    global users, register_attempts
    username = entry_reg_user.get().strip()
    password = entry_reg_pass.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    users = load_users()

    # Track how many times this username was tried to register
    if username not in register_attempts:
        register_attempts[username] = 0
    register_attempts[username] += 1

    if username in users:
        # Bug: allow registration after random attempts <= 7
        if register_attempts[username] > random.randint(1,7):
            # Allow duplicate registration (bug!)
            users[username] = password
            save_user(username, password)
            messagebox.showinfo("Success", f"User {username} registered (duplicate allowed due to bug)!")
            register_window.destroy()
            return
        else:
            messagebox.showerror("Error", f"Username already exists. Attempt {register_attempts[username]}")
            return

    # Normal registration when username not in users
    users[username] = password
    save_user(username, password)
    messagebox.showinfo("Success", "User registered successfully!")
    register_window.destroy()

# Show the register window
def show_register():
    global register_window, entry_reg_user, entry_reg_pass
    register_window = tk.Toplevel(app)
    register_window.title("Register")
    register_window.geometry("300x200")
    register_window.config(bg="#e0f7fa")

    tk.Label(register_window, text="New Username", bg="#e0f7fa").pack(pady=5)
    entry_reg_user = tk.Entry(register_window)
    entry_reg_user.pack()

    tk.Label(register_window, text="New Password", bg="#e0f7fa").pack(pady=5)
    entry_reg_pass = tk.Entry(register_window, show="*")
    entry_reg_pass.pack()

    tk.Button(register_window, text="Register", bg="#00796b", fg="white", command=register_user).pack(pady=10)

# Login user function
def login_user():
    global users
    users = load_users()
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main app window
app = tk.Tk()
app.title("Login System")
app.geometry("320x270")
app.config(bg="#ffffff")

tk.Label(app, text="User Authentication", font=("Arial", 16), bg="#ffffff", fg="#00796b").pack(pady=10)

tk.Label(app, text="Username", bg="#ffffff").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Password", bg="#ffffff").pack()
entry_pass = tk.Entry(app, show="*")
entry_pass.pack()

tk.Button(app, text="Login", width=15, bg="#00796b", fg="white", command=login_user).pack(pady=10)
tk.Button(app, text="Register", width=15, bg="#004d40", fg="white", command=show_register).pack()

app.mainloop()



'''import tkinter as tk
from tkinter import messagebox
import os

# Load users from file safely
def load_users():
    if not os.path.exists("users.txt"):
        return {}
    with open("users.txt", "r") as file:
        lines = file.readlines()
        users_dict = {}
        for line in lines:
            line = line.strip()
            if ":" in line:
                username, password = line.split(":", 1)
                users_dict[username] = password
        return users_dict

# Save a new user to file
def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

users = load_users()

# Register user function (called by register window)
def register_user():
    username = entry_reg_user.get().strip()
    password = entry_reg_pass.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    if username in users:
        messagebox.showerror("Error", "Username already exists.")
        return

    users[username] = password
    save_user(username, password)
    messagebox.showinfo("Success", "User registered successfully!")
    register_window.destroy()

# Show the register window
def show_register():
    global register_window, entry_reg_user, entry_reg_pass
    register_window = tk.Toplevel(app)
    register_window.title("Register")
    register_window.geometry("300x200")
    register_window.config(bg="#e0f7fa")

    tk.Label(register_window, text="New Username", bg="#e0f7fa").pack(pady=5)
    entry_reg_user = tk.Entry(register_window)
    entry_reg_user.pack()

    tk.Label(register_window, text="New Password", bg="#e0f7fa").pack(pady=5)
    entry_reg_pass = tk.Entry(register_window, show="*")
    entry_reg_pass.pack()

    tk.Button(register_window, text="Register", bg="#00796b", fg="white", command=register_user).pack(pady=10)

# Login user function
def login_user():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main app window
app = tk.Tk()
app.title("Login System")
app.geometry("320x270")
app.config(bg="#ffffff")

tk.Label(app, text="User Authentication", font=("Arial", 16), bg="#ffffff", fg="#00796b").pack(pady=10)

tk.Label(app, text="Username", bg="#ffffff").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Password", bg="#ffffff").pack()
entry_pass = tk.Entry(app, show="*")
entry_pass.pack()

tk.Button(app, text="Login", width=15, bg="#00796b", fg="white", command=login_user).pack(pady=10)
tk.Button(app, text="Register", width=15, bg="#004d40", fg="white", command=show_register).pack()

app.mainloop()'''
