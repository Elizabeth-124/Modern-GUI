import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("500x300")
app.title("Login system")

def click():
    print("You clicked Login")

title=ctk.CTkLabel(app,text="Login System",font=("Arial",32))
title.pack(pady=10)

username=ctk.CTkEntry(app,placeholder_text="Username")
username.pack(pady=10)

password=ctk.CTkEntry(app,placeholder_text="Password")
password.pack(pady=10)

btn=ctk.CTkButton(master=app,text="Login",command=click)
btn.pack(pady=10)

app.mainloop()