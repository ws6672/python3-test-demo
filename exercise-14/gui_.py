import image_

from tkinter import *
from tkinter import messagebox
from functools import partial


result_path=""
root = Tk()
root.title("图片处理器")
root.geometry("500x128")

label = Label(root,text="文件路径：", font=('Arial', 12), width=16, height=2)
label.grid(row=0, column=0)
code_text = Entry(root,width=24)
code_text.grid(row=0, column=1)


button3 = Button(root, text="转换", command=partial(image_.filter_image,code_text.get()))
button3.grid(row=2, column=1)


if __name__ == '__main__':
   root.mainloop()