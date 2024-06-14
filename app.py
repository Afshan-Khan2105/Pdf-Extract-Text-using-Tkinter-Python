from tkinter import *
from tkinter.filedialog import askopenfile
import PyPDF2
from PIL import Image, ImageTk
from functions import display_logo, display_textbox, copy_text

root = Tk()
root.title("PDF Text Extractor")
root.geometry("800x600")

# Header frame
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

# Main content frame
main_content = Frame(root, width=800, height=250, bg="#FFC0CB")
main_content.grid(columnspan=3, rowspan=2, row=2)

# Logo
display_logo('logo.png', 0, 0)

# Instructions
instructions = Label(root, text="Select a PDF File to extract its text", font=("Raleway", 14))
instructions.grid(columnspan=3, column=0, row=1, pady=10)

# Browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda: open_file(),
                    font=("Raleway", 12), bg="#FFC0CB", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=0, sticky=E, padx=20)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        page_content = page_content.replace('\u2122', "'")

        display_textbox(page_content, 2, 0, root)

        browse_text.set("Browse")

root.mainloop()
