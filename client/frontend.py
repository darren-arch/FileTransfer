from tkinter import *

window = Tk()
window.title('File Transfer')

Lb = Listbox(window)
Lb.insert(1, 'Python')
Lb.insert(2, 'Python1')
Lb.insert(3, 'Python2')
Lb.insert(4, 'Python3')
Lb.pack()

#var1 = IntVar()
#Checkbutton(window, text='male', variable=var1).grid(row=0, sticky='w')
#var2 = IntVar()
#Checkbutton




#Label(window, text="First Name").grid(row=0)
#Label(window, text="Last Name").grid(row=1)

#e1 = Entry(window)
#e2 = Entry(window)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)



#button = Button(window, text="Stop", width=25, command=window.destroy)
#button.pack()


#l = Label(window, text="File Transfer")
#l.pack()

window.mainloop()