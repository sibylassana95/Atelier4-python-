from tkinter import *

gui = Tk()
text = Text(gui, height=10, width=50)
text.insert(INSERT, "Hello.....")
text.insert(END, "Siby")
text.pack()

text.tag_add("hello", "1.0", "1.5")
text.tag_add("siby", "1.21", "1.32")
text.tag_config("hello", background="red", foreground="blue")
text.tag_config("siby", background="black", foreground="white")
gui.mainloop()
