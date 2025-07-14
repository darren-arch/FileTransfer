import tkinter as tk
from tkinter import messagebox

def download_item():
    # Get the selected item index
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("No selection", "Please select an item to download.")
        return

    selected_index = selected_indices[0]
    selected_item = listbox.get(selected_index)
    print(f"Downloading: {selected_index}")
    # Do something with the selected item
    # e.g., call your download logic here

# Set up the GUI
root = tk.Tk()
root.title("Download Selector")

# Create a listbox with some items
listbox = tk.Listbox(root, height=10)
items = ["File1.txt", "File2.pdf", "Image1.png", "Document.docx"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

# Create a download button
download_button = tk.Button(root, text="Download", command=download_item)
download_button.pack(pady=5)

# Start the main loop
root.mainloop()





#from tkinter import *

#window = Tk()
#window.title('File Transfer')



#Lb = Listbox(window)
#Lb.insert(0, 'file0')
#Lb.insert(1, 'file1')
#Lb.insert(2, 'file2')
#Lb.insert(3, 'file3')
#Lb.pack()

#button = Button(window, text="Download", width=25)
#button.pack()

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