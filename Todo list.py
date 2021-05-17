
from tkinter import *
from tkinter import messagebox

l = []
c = 1


def entryError():
    if insertField.get() == "":
        messagebox.showinfo("Error in input. Please input again")

        return 0

    return 1


def insertTask():
    global c

    value = entryError()

    if (value == 0):
        return
    var = insertField.get() + "\n"

    l.append(var)
    TextArea.insert('end -1 chars', str(c) + "->" + var)
    c = c + 1
    del_tf()


def del_nf():
    nf.delete(0.0, END)


def del_tf():
    insertField.delete(0, END)


def delete():
    global c

    if (len(l) == 0):
        messagebox.showerror("There are no tasks")
        return
    number = nf.get(1.0, END)

    if (number == "\n"):
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)

    del_nf()

    l.pop(task_no - 1)
    c = c - 1

    TextArea.delete(1.0, END)

    for i in range(len(l)):
        TextArea.insert('end -1 chars', str(i + 1) + "->" + l[i])


if (__name__ == "__main__"):
    window = Tk()
    window.configure(background="black")
    window.title("To-Do List")
    window.geometry("400x500")
    window.resizable(0,0)


    enterTask = Label(window, text="Please enter your task", bg="green")

    insertField = Entry(window)

    Submit = Button(window, text="Submit", fg="Black", bg="blue", command=insertTask)

    TextArea = Text(window, height=4, width=25, font="arial 13")

    taskNumber = Label(window, text="Specify the task number that you want to remove,below",bg="cyan")

    nf = Text(window, height=1, width=3, font="arial 13")

    delete = Button(window, text="Delete", fg="Black", bg="orange", command=delete,width = 10)

    Exit = Button(window, text="Do you want to close?", fg="Black", bg="Red", command=exit,width = 34)
    enterTask.place (x=130, y= 20)
    insertField.place( x = 50 , y = 60  , width = 300)
    Submit.place(x= 170,y=100)
    TextArea.place(x = 10,y = 135  , height = 200 , width = 380)
    taskNumber.place(x= 45, y =340)
    nf.place(x = 177 , y = 370)
    delete.place(x = 153, y = 410)
    Exit.place(x= 50 , y= 450 ,height= 20  , width = 300 ,)
    window.mainloop()