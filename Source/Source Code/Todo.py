import customtkinter




## -----All functions start here--------

## function name setupPomodoroScreen -> Void
## Created by Minh Quang Le, 11/07/2022
## Action: Setup các widget cho screen Todo
def setupTodoScreen():

    ## Get glonal là todoApp về
    global todoApp
    frame_todo = customtkinter.CTkFrame(master=todoApp)
    frame_todo.pack(padx=20,pady=60,fill="both",expand=True)
    name_label = customtkinter.CTkLabel(master=frame_todo,text="TODO",font = ("Montserrat",34))
    name_label.pack(padx = 20, pady = 10)
    frame_todo_search = customtkinter.CTkFrame(master=frame_todo,width=150, height = 50)
    frame_todo_search.pack(padx = 10, pady = 10)
    todoEntry = customtkinter.CTkEntry(master=frame_todo_search,placeholder_text="What to do?", width=150)
    addButton = customtkinter.CTkButton(master=frame_todo_search, text = 'Add work', width=30)
    todoEntry.pack(side = 'left', expand = True)
    addButton.pack(side = 'left', expand = True)



## -----All functions end here--------





## function name createHomeworkApp -> Void
## Created by Minh Quang Le, 11/07/2022
## Action: Treat như là Constructor của screen Todo
def createTodoScreen(app):
    global todoApp
    todoApp = customtkinter.CTkToplevel(app)
    todoApp.focus()
    todoApp.geometry("650x500")
    todoApp.title("Todo Screen")
    setupTodoScreen()
