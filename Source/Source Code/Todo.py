import customtkinter
from functools import partial



## -----All functions start here--------

## function name setupPomodoroScreen -> customtkinter.CTkFrame
## Created by Minh Quang Le, 12/07/2022
## Action: Trả về một frame chứa một item là task
def createItem(taskName):
    global scrollable_frame_todo
    itemFrame = customtkinter.CTkFrame(scrollable_frame_todo,width=200)

    item_nameLabel = customtkinter.CTkLabel(master = itemFrame, text = taskName,font = ("Montserrat",10))
    upButton = customtkinter.CTkButton(master=itemFrame, text = 'Moves Up', width=5, height = 5)
    downButton = customtkinter.CTkButton(master=itemFrame, text = 'Moves Down', width=5)
    finishedButton = customtkinter.CTkButton(master=itemFrame, text = 'Finished', width=5, command = lambda:itemFrame.forget())
    item_nameLabel.pack(side = 'left', expand = True)
    upButton.pack(padx=5, side = 'right', expand = True)
    downButton.pack(padx=5, side = 'right', expand = True)
    finishedButton.pack(padx=5, side = 'right', expand = True)
    return itemFrame

def addItem(itemName):
    global scrollable_frame_todo
    itemFrame = createItem(itemName)
    itemFrame.pack()


## function name setupPomodoroScreen -> Void
## Created by Minh Quang Le, 11/07/2022
## Action: Setup các widget cho screen Todo
def setupTodoScreen():

    ## Get glonal là todoApp về
    global todoApp
    global frame_todo
    global scrollable_frame_todo
    frame_todo = customtkinter.CTkFrame(master=todoApp)
    frame_todo.pack(padx=20,pady=60,fill="both",expand=True)
    name_label = customtkinter.CTkLabel(master=frame_todo,text="TODO",font = ("Montserrat",34))
    name_label.pack(padx = 20, pady = 10)

    ## Entry Frame
    frame_todo_search = customtkinter.CTkFrame(master=frame_todo,width=150, height = 50, fg_color = 'transparent')
    frame_todo_search.pack(padx = 10, pady = 10)

    todoEntry = customtkinter.CTkEntry(master=frame_todo_search,placeholder_text="What to do?", width=150)
    addButton = customtkinter.CTkButton(master=frame_todo_search, text = 'Add work', width=30, command= lambda: addItem(todoEntry.get()))
    finishButton = customtkinter.CTkButton(master=frame_todo_search, text = 'Finished', width=30)
    todoEntry.pack(padx=10, side = 'left', expand = True)
    addButton.pack(padx=10, side = 'left', expand = True)
    finishButton.pack(padx = 10,side = 'left', expand = True)

    ##Create frame that can scroll

    scrollable_frame_todo = customtkinter.CTkScrollableFrame(frame_todo)
    scrollable_frame_todo.pack(padx=20,pady=60,fill="both",expand=True)

    # for i in range(0,3):
    #     item1 = createItem("Xem animeeeeeeee")
    #     item1.pack(pady = 5)




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
