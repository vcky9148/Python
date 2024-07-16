import tkinter as tk
from time import strftime

# tkinter is a standard GUI (Graphical User Interface) toolkit in Python. We import it as tk for brevity.
# strftime is a method from the time module which helps to format time as per the given format.

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#time() is a function that gets the current time and updates the label text with it.
#strftime('%H:%M:%S %p') formats the time in the format HH:MM:SS AM/PM.
#label.config(text=string) updates the text of the label widget with the formatted time.
#label.after(1000, time) schedules the time function to be called again after 1000 milliseconds (1 second), creating an update loop.

root = tk.Tk()
root.title("Digital Clock")

#tk.Tk() creates the main window of the application.
#root.title("Digital Clock") sets the title of the window to "Digital Clock".

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

#tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan') creates a label widget with specified font, background color, and foreground color.
#label.pack(anchor='center') packs the label widget into the window and centers it horizontally.

time()
root.mainloop()

#time() is called initially to set the label text to the current time.
#root.mainloop() starts the event loop which keeps the window open until it is closed by the user.