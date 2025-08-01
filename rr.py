import tkinter as tk

# Initialize main window
window = tk.Tk()
window.title("Counter App")
window.geometry("300x200")

# Initialize counter value
counter = 0

# Function to update counter
def increment():
    global counter
    counter += 1
    counter_label.config(text=str(counter))

# Label to display the counter
counter_label = tk.Label(window, text="0", font=("Arial", 40))
counter_label.pack(pady=20)

# Button to increment the counter
increment_button = tk.Button(window, text="Click Me", font=("Arial", 20), command=increment)
increment_button.pack()

# Run the application
window.mainloop()
