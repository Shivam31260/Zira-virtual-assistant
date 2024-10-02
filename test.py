import pywhatkit
import pyautogui as pt
from datetime import datetime

# Get current time
current_time = datetime.now()
hour = current_time.hour
minute = current_time.minute+1
x= input(print("You must provide a number to whom you want to send the message:-  "))
y=input(print("What should the message say:-  "))
# print(hour)
pywhatkit.sendwhatmsg(x,y, hour, minute)
pt.click()
# expression = "2 x 3"
# expression = expression.replace('x', '*')

# # Now evaluate the expression
# result = eval(expression)
# print(result)import tkinter as tk
# import tkinter as tk

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Simple Tkinter Example")

# # Create a label widget
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack(pady=20)

# # Start the Tkinter event loop
# root.mainloop()
# while True:
#     x=input("Enter A Value: -")
#     y=True
#     while y:
#         if x=="1":
#             from Snakegame import game_loop
#             game_loop()
#             print(y)
#         elif x=="2":
#             from Detection import object
#             object()
#             break

