import customtkinter

pomodoroApp = None


## function name createHomeworkApp -> Void
## Created by Minh Quang Le, 11/07/2022
## Action: Treat như là Constructor của screen Pomodoro
def createPomodoroScreen(app):
    pomodoroApp = customtkinter.CTkToplevel(app)
    pomodoroApp.focus()
    pomodoroApp.geometry("650x500")
    pomodoroApp.title("Pomodoro Screen")
