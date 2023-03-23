import customtkinter as ctk

def calculate():
    expression=()
    try:
        result = eval(expression)
        log+= " ", result

        return result and log
    except:
        return "Invalid expression. Please enter a valid arithmetic expression."
    
    
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

main= ctk.CTk()
main.geometry("500x350")
main.title("Clean Calculator")

frame = ctk.CTkFrame(master=main)
frame.pack(pady=20,padx=40,fill='both',expand=True)

expression = ctk.CTkEntry(master=frame,placeholder_text="Enter")
expression.pack(pady=15,padx=10, fill='both',expand=True)

lilframe = ctk.CTkFrame(master=main)
lilframe.pack(pady=20,padx=40)



main.mainloop()
