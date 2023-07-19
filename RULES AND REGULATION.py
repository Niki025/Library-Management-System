import tkinter as tk
from tkinter.tix import Tk

root = Tk()

# specify size of window.
root.geometry("550x310")

# Create text widget and specify size.
T = tk.Text(root, height = 20, width = 90)

# Create label
l = tk.Label(root, text ="RULES AND REGULATION")
l.config(font =("Courier", 14))

Fact = """1)Library users must prominently display their Student ID on them at all times. Students 
who fail to do so will not be allowed access to the Library facilities.

2)No items belonging to the library are to be taken out of the library unless they have 
been checked out at the Circulation Desk.

3)Personal belongings should not be left unattended. The library management will not be
held responsible for the loss of personal belongings.

4)No food and drink (except plain water) are allowed in the library.

5)Mobile phones or any other personal electronic gadgets must be switched to silent mode
before entering the library.

6)Making unreasonable noise, loud conversations, loud cell phone calls or playing loud 
music or video that can distract other library users in the library is not permitted.

7)Users are prohibited from making or answering calls within the quiet zone.

8)Discussion room is used for academic purposes only and should not be used for private
study or social purposes.

9)Eating, drinking, sleeping and smoking are not allowed in the library.

10)The Library users should be professionally attired, as specified in the student
handbook. We reserve the right to deny entry to students who are inappropriately attired.

11)Library furniture/equipment should not be moved from its original location.

12)Personal Computers provided are to be strictly used for academic research and Library
CD viewing only. These computers cannot be used for personal e-mail, online chatting or playing games.

13)Library staffs reserve the right to inspect bags or other personal property when users
enter or leave the library.

14)When a user is caught for breaching the library rules and regulations, immediate 
action will be taken."""

# Create an Exit button.
b2 = tk.Button(root, text ="Exit",
               command = root.destroy)

l.pack()
T.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()