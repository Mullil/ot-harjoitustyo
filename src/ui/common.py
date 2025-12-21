from tkinter import ttk


def create_button(frame, text, command):
    button = ttk.Button(
        master=frame,
        text=text,
        command=command
    )
    button.pack(padx=5, pady=5)

def create_header(frame, text):
    header = ttk.Label(
        master=frame,
        text=text
    )
    header.pack(padx=10, pady=10)

def create_entry(frame, text):
    label = ttk.Label(master=frame, text=text)
    entry = ttk.Entry(master=frame)
    label.pack(padx=5, pady=5)
    entry.pack(padx=5, pady=5)
    return entry