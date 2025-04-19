import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    # Update every 1000ms (1 second)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Python Clock")
root.geometry("300x100")
root.resizable(False, False)
root.configure(bg="black")

# Create a label to display the time
time_label = tk.Label(
    root, 
    font=('Helvetica', 36, 'bold'),
    background='black',
    foreground='#00FF00'  # Green text
)
time_label.pack(anchor='center', fill='both', expand=1)

# Start the clock
update_time()

# Run the application
root.mainloop()