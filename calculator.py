import customtkinter as ctk
from pathlib import Path
from tkinter import font

# Create main window first
main = ctk.CTk()
main.geometry("500x350")
main.title("🎀 Cute Calculator 🎀")

# Then load font
current_dir = Path(__file__).parent
font_path = current_dir / "Testimonia-3zp8X.ttf"

try:
    ctk.FontManager.load_font(str(font_path))
    font.families()
    custom_font_name = "Testimonia"
except Exception as e:
    print(f"Font loading error: {e}")
    custom_font_name = "Comic Sans MS"

def calculate():
    try:
        result = eval(expression.get())
        label.configure(text=str(result))
    except:
        label.configure(text="Error")
        expression.delete(0, ctk.END)

def button_press(num):
    current = expression.get()
    expression.delete(0, ctk.END)
    expression.insert(0, str(current) + str(num))
    if num in '0123456789':
        label.configure(text="0")

def clear():
    expression.delete(0, ctk.END)
    label.configure(text="0")

ctk.set_appearance_mode("light")

frame = ctk.CTkFrame(master=main, fg_color="white")
frame.pack(pady=20, padx=40, fill='both', expand=True)

expression = ctk.CTkEntry(
    master=frame,
    placeholder_text="🎀 Input Expression 🎀",
    height=60,
    font=(custom_font_name, 65, "bold"),
    justify="right",
    fg_color="white",
    text_color="#ff4da6",
    placeholder_text_color="#ff80bf",
    border_color="#ff80bf",
    border_width=2
)
expression.pack(pady=(15,0), padx=10, fill='both')

label = ctk.CTkLabel(
    master=frame,
    text="",
    font=(custom_font_name, 55, "bold"),
    text_color="#ff4da6",
    anchor="e",
    justify="right"
)
label.pack(pady=(0,15), padx=10, fill='both')

# Update resize function
def on_resize(event):
    window_width = main.winfo_width()
    input_size = int(window_width / 12)
    result_size = int(window_width / 15)
    button_size = int(window_width / 18)
    
    expression.configure(font=(custom_font_name, input_size, "bold"))
    label.configure(font=(custom_font_name, result_size, "bold"))
    
    # Update all button fonts
    for child in button_frame.winfo_children():
        child.configure(font=(custom_font_name, button_size, "bold"))

# Bind the resize function to window resizing
main.bind("<Configure>", on_resize)

# Create calculator buttons
button_frame = ctk.CTkFrame(master=frame)
button_frame.pack(pady=10, padx=10, fill='both', expand=True)

# Configure grid weights
for i in range(4):  # 4 rows
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)  # 4 columns

# Update the buttons list to include 'C' for clear
buttons = [
    'C', '/', '*', '-',  # Added 'C' to first row
    '7', '8', '9', '+',
    '4', '5', '6', '=',
    '1', '2', '3', '0'
]

row = 0
col = 0
for button in buttons:
    # Update command logic to handle clear button
    if button == 'C':
        cmd = clear
    elif button == '=':
        cmd = calculate
    else:
        cmd = lambda x=button: button_press(x)
    
    ctk.CTkButton(
        master=button_frame,
        text=button + " 🎀" if button == 'C' else button,
        command=cmd,
        width=60,
        height=60,
        fg_color="white",
        hover_color="#ffe6f2",
        text_color="#ff4da6",
        border_color="#ff80bf",
        border_width=2,
        font=(custom_font_name, 42, "bold")
        ).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

main.mainloop()
