import tkinter as tk
from tkinter import ttk

def value_combobox(event):
    value_choose = combobox.get()
    combobox.set(value_choose)
    combobox['values'] = options  # Reset to original options

def suggest(event):
    input_value = combobox.get()
    if input_value == "":
        combobox['values'] = options  # Show all options if no input
    else:
        # Filter options based on the input
        values = [x for x in options if input_value.lower() in x.lower()]
        combobox['values'] = values  # Update the combobox values dynamically
    # You can automatically open the dropdown when filtering by uncommenting this line
    # combobox.event_generate('<Button-1>')

# Main window
root = tk.Tk()
root.title("Combobox Example")

# List of options for the combobox
options = [
    "Hạnh phúc",
    "Thành công",
    "Sức khỏe tốt",
    "Yêu thương",
    "Hòa bình",
    "May mắn",
    "Sáng tạo",
    "Hiểu biết",
    "Tự tin",
    "Tình bạn"
]

# Create Combobox
combobox = ttk.Combobox(root, values=options)
combobox.pack()

# Bind events
combobox.bind("<KeyRelease>", suggest)  # Trigger suggestion on key release
combobox.bind("<<ComboboxSelected>>", value_combobox)  # Trigger when user selects an item

root.geometry("250x200")
root.mainloop()
