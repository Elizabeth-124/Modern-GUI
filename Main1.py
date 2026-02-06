import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry=("500x300")
app.title("My first tkinter window")

def click():
    print("You clicked a button")

btn=ctk.CTkButton(master=app,text="click me",command=click)
btn.pack(pady=20,padx=20)

app.mainloop()