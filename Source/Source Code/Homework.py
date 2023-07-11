import customtkinter

homeworkApp = None




## function name createHomeworkApp -> Void
## Created by Minh Quang Le, 11/07/2022
## Action: Treat như là Constructor của screen Homework
def createHomeworkScreen(app):
    homeworkApp = customtkinter.CTkToplevel(app)
    homeworkApp.focus()
    homeworkApp.geometry("650x500")
    homeworkApp.title("Homework Screen")
