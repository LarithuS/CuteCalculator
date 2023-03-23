import customtkinter as ctk

def calculate():
    expression=()
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid expression. Please enter a valid arithmetic expression."


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

main= ctk.CTk()
main.geometry("500x350")
main.title("Clean Calculator")

frame = ctk.CTkFrame(master=main)
frame.pack(pady=20,padx=40,fill='both',expand=True)

expression = ctk.CTkEntry(master=frame,placeholder_text="Input Expression")
expression.pack(pady=15,padx=10, fill='both',expand=True)

lilframe = ctk.CTkFrame(master=main)
lilframe.pack(pady=20,padx=40)

label = ctk.CTkLabel(master=lilframe,text="log",width=120,height=25,corner_radius=8,font=('Roboto', 14))
label.pack(pady=20,padx=40,fill='both')


main.mainloop()
