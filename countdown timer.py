import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

#tkinter is a standard GUI (Graphical User Interface) toolkit in Python.
#messagebox module provides a set of functions to create common dialogue boxes.
#datetime module supplies classes for manipulating dates and times.
#timedelta is a class used to represent the difference between two dates or times.

def start_timer():
    global remaining_time
    remaining_time = int(entry.get()) * 60
    countdown()

#start_timer(): This function is called when the user clicks the "Start" button. 
                #It retrieves the time entered by the user, converts it to seconds, and starts the countdown.
#countdown(): This function is responsible for updating the timer label every second until the countdown reaches zero. 
             #If the countdown reaches zero, it displays a message box indicating that time's up.



def countdown():
    global remaining_time
    if remaining_time <= 0:
        messagebox.showinfo("Countdown Timer", "Time's up!")
    else:
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        timer_label.after(1000, countdown)

root = tk.Tk()
root.title("Countdown Timer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter time in minutes:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

start_button = tk.Button(frame, text="Start", command=start_timer)
start_button.grid(row=1, columnspan=2)

timer_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
timer_label.pack(pady=10)

root.mainloop()
