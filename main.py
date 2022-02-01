from tkinter import *
from tkinter import ttk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


FONT_NAME = "Montserrat"
word_count = 0
count = 0
typed_text = []

def count_up(count):
    global typed_text, word_count
    current_text = text_area.get("1.0", "end-1c")
    if len(typed_text) != 0 and typed_text == current_text:
        if count == 0:
            text_area.delete("1.0", "end")
    else:
        typed_text = current_text.strip()
        word_list = typed_text.split(" ")
        word_list2 = list(filter(None, word_list))
        word_count_label.config(text=f"{len(word_list2)} words")
        count = 5
    window.after(1000, count_up, count-1)
    description_label.config(text=f"If you stop, your writing will be vanish after {count} sec")


window = Tk()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

top = Frame(window, padx=20, pady=20)
middle = Frame(window, padx=50, pady=50,)
bottom = Frame(window, pady=20)
top.pack()
middle.pack()
bottom.pack()

title_label = Label(top, text="The Most Clueless Writer", font=(FONT_NAME, 30), fg="#D9534F")
title_label.pack()
description_label = Label(top, text="If you stop, your writing will be vanish after 5 sec", font=(FONT_NAME, 12))
description_label.pack(side=BOTTOM)

text_area = Text(middle, bd=0, bg="#FFFFFF", font=(FONT_NAME, 16), width=50, height=10)
text_area.focus()
text_area.pack(side=LEFT)
vscroll = Scrollbar(middle, orient=VERTICAL, command=text_area.yview)
text_area["yscroll"] = vscroll.set
vscroll.pack(side=RIGHT, fill=Y)
# window.bind("<space>", user_type)

word_count_label = Label(bottom, text=f"{word_count} words", font=(FONT_NAME, 16))
word_count_label.pack()

count_up(count)
window.mainloop()