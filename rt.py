import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Text Input App")
window.geometry("350x200")

# Function to display typed text
def show_text():
    user_input = entry.get()
    output_label.config(text=f"You typed: {user_input}")

# Label for instruction
instruction_label = tk.Label(window, text="Type something below:", font=("Arial", 12))
instruction_label.pack(pady=5)

# Text entry field
entry = tk.Entry(window, width=30, font=("Arial", 14))
entry.pack(pady=5)

# Button to show the text
show_button = tk.Button(window, text="Show Text", font=("Arial", 12), command=show_text)
show_button.pack(pady=10)

# Label to display the typed text
output_label = tk.Label(window, text="", font=("Arial", 14))
output_label.pack()

# Run the app
window.mainloop()
