from tkinter import *
import pickle

def add_t():
    t = task_ent.get()
    if t:
        todo_list.append(t)
        l_b.insert(END,t)
        task_ent.delete(0,END)
def remove_t():
    s_item = l_b.curselection()
    if s_item:
        l_b.delete(s_item)
        for i in todo_list:
            l_b.delete(END,i)
            
def save_t():
    with open('todo_list.pkl','wb') as f:
        pickle.dump(todo_list,f)

def copy_t():
    try:
        with open('todo_list.pkl','rb') as f:
            todo_list = pickle.loads(f.read())
    except FileNotFoundError:
        todo_list =[]
        
    for i in todo_list:
        l_b.insert(END,i)                            
    
                        
app = Tk()
app.title("To Do List")
app.geometry("720x480")
app.resizable(False,False)
app.config(bg="#242424")
todo_list =[]
# heading
title = Label(app,text="To-Do list",font=("Consolas",18),bg="#242424",fg="#fff")
title.pack(pady=20)

text = StringVar()
task_ent= Entry(app,width=34,textvariable=text,font=("Consolas",12))
task_ent.pack()

#add Button
add = Button(app,text="Add",width=12,font=("Consolas",12),command=add_t)
add.place(x =205,y= 110)

remove = Button(app,text="Delete",width=12,font=("Consolas",12),command=remove_t)
remove.place(x =450,y= 110)

save = Button(app,text="Save",width=12,font=("Consolas",12),command=save_t)
save.place(x =205,y= 150)

copy_todo = Button(app,text="Load",width=12,font=("Consolas",12),command=copy_t)
copy_todo.place(x =450,y= 150)

#list box
l_b = Listbox(app,height=15,width=45,font=("Consolas",12))
l_b.place(x=170,y=200)

app.mainloop()
