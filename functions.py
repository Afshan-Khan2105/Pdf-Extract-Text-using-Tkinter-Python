from tkinter import *
from PIL import Image, ImageTk

def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)

def display_textbox(content, row, col, root):
    text_frame = Frame(root, bg="white")
    text_frame.grid(column=col, row=row, columnspan=2, pady=10, padx=10, sticky=N+S+E+W)

    text_box = Text(text_frame, height=15, width=70, padx=15, pady=15)
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(text_frame, command=text_box.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_box.config(yscrollcommand=scrollbar.set)

    # Copy Text button
    copy_btn = Button(root, text="Copy Text", command=lambda: copy_text(text_box), font=("Raleway", 12), bg="#FFC0CB", fg="white", height=2, width=15)
    copy_btn.grid(column=col, row=row+1, pady=10)

def copy_text(text_widget):
    content = text_widget.get("1.0", "end-1c")
    text_widget.clipboard_clear()
    text_widget.clipboard_append(content)
    text_widget.update()  # Now it stays on the clipboard after the window is closed
