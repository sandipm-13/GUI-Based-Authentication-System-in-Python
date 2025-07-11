# GUI-Based-Authentication-System-in-Python
GUI-Based Authentication System in Python - This project is a Python-based authentication system with a graphical interface using Tkinter. It allows user registration and login, stores credentials securely in a file, and demonstrates key testing and debugging techniques by identifying and fixing common software bugs.

( Report )
Title: GUI-Based Authentication System in Python

Subject: Testing and Debugging
Submitted by: Sandip Mahato
Semester: B.Sc. Computer Science, Semester 2


---

1. Introduction to Testing and Debugging
Testing and debugging are crucial steps in software development that ensure the reliability, functionality, and correctness of a program. In this project, I developed a GUI-based authentication system using Python and Tkinter that allows users to register and log in. Testing helped verify the application's behavior under different conditions, while debugging allowed me to identify and fix 16 common bugs, making the system robust and user-friendly.


---

2. Project Overview and Code Architecture
This project implements a user login and registration system with a graphical interface. All credentials are stored in a text file (users.txt) for simplicity.

load_users(): Reads users from file

save_users(): Writes updated users to file

register_user(): Validates and registers new users

login_user(): Authenticates login attempts

is_valid(): Validates character rules for input

GUI layout: Designed using Tkinter widgets (Entry, Label, Button)


The modular structure makes the program easy to debug, test, and expand.


---

3. Technologies

Python 3.x (Core Programming)

Tkinter (GUI framework)

users.txt (File-based storage)

Manual testing tools (messagebox, print statements)

IDE: Visual Studio Code / IDLE

Operating System: Windows 10



---

4. Debugging Techniques Used

print() Statement Debugging

MessageBox Debugging (tkinter.messagebox)

Manual step-by-step testing

Input echoing and trace logging

Function isolation testing

File content inspection

Structured code refactoring



---

5. Types of Testing Used & Sample Test Cases

Unit Testing

Input Validation Testing

Functional Testing

Boundary Testing

Negative Testing

Manual GUI Testing

File Handling Testing


Test Case	Scenario	Input	Expected Output	Result

TC01	Register Valid	user1/pass123	Registered	Pass
TC02	Existing User	user1 again	Error	Pass
TC03	Blank Input	""	Error	Pass
TC04	Invalid Char	user:123	Error	Pass
TC05	Password Mismatch	pass1/pass2	Error	Pass
TC06	Login Valid	user1/pass123	Login Success	Pass
TC07	Wrong Password	user1/wrong	Error	Pass
TC08	Login Limit	wrong x3	App Exits	Pass
TC09	File Entry	user2	File Updated	Pass



---

6. Bug Identification and Description

Bug No.	Description	Present	Status

1	Duplicate registration	✅	Fixed
2	Plain text passwords	✅	Fixed
3	No confirmation field	✅	Fixed
4	No login attempt limit	✅	Fixed
5	No input length validation	✅	Fixed
6	No file locking	✅	Fixed
7	Colon not escaped in input	✅	Fixed
8	Case sensitivity not explained	✅	Fixed
9	No feedback logging	✅	Fixed
10	Fields not cleared after login	✅	Fixed
11	No exit/reset button	✅	Fixed
12	Multiple register windows	✅	Fixed
13	Duplicate usernames in file	✅	Fixed
14	No input sanitization	✅	Fixed
15	Outdated users dict	✅	Fixed
16	Flat file scalability	✅	Prepared for future database


(All 16 bugs identified and resolved.)


---

7. Conclusion

This project helped me understand the importance of testing and debugging in real-world applications. By fixing each identified bug, I ensured the application performs reliably and securely. I also learned to separate concerns in code, validate inputs, and structure GUI elements for user-friendly interaction. This experience significantly enhanced my skills in Python, debugging, and software quality assurance.


---

(End of Report)

