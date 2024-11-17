import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Dangerous Writing App")
window.geometry("600x400")

timeout = 5000  # 5000 milliseconds = 5 seconds
timer = None

def start_timer():
    global timer
    timer = window.after(timeout, clear_text)

def reset_timer(event=None):
    global timer
    if timer:
        window.after_cancel(timer)
    start_timer()

def clear_text():
    text_area.delete("1.0", tk.END)
    messagebox.showwarning("Time's up!", "You stopped typing. Text cleared!")

text_area = tk.Text(window, font=("Arial", 14), wrap="word")
text_area.pack(expand=True, fill="both")

text_area.bind("<Key>", reset_timer)

start_timer()

window.mainloop()
