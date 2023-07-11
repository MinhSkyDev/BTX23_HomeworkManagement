import customtkinter
from Pomodoro import *
from Homework import *
from Todo import *



## App name Homework Management System
## Created by Minh Quang Le, 11/07/2022
## Created by "Person who contribute to this one"
## Purpose: Educational Purpose
## ---------------------Start---------------------
def createPomodoro():
    createPomodoroScreen(app)

def createTodo():
    createTodoScreen(app)

def createHomework():
    createHomeworkScreen(app)


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title('App Vô Địch')
app.geometry("650x500")

frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=20,pady=60,fill="both",expand=True)

name_label = customtkinter.CTkLabel(master=frame,text="Homework Management System",font = ("Montserrat",34))
name_label.pack(padx = 20, pady = 30)

pomodoroButton = customtkinter.CTkButton(frame, text="POMODORO", font=("Montserrat",12),
                    width = 150,height = 150, command = createPomodoro)
todoButton = customtkinter.CTkButton(frame, text="TO-DO LIST", font=("Montserrat",12),
                    width = 150,height = 150, command = createTodo)
homeworkButton = customtkinter.CTkButton(frame, text="HOMEWORK MANAGEMENT",font=("Montserrat",12),
                    width = 150,height = 150, command = createHomework)

pomodoroButton.pack(padx = 10, pady =30, side = 'left', expand = True)
todoButton.pack(padx=10, pady =30, side = 'left', expand = True)
homeworkButton.pack(padx = 10,pady =30, side = 'left', expand = True)

app.mainloop()

## ---------------------End---------------------
