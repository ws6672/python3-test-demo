import image_

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title("图片处理器")
root.geometry("500x128")

label = Label(root,text="资源路径：", font=('Arial', 12), width=10, height=2)
label.grid(row=0, column=0)
code_text = Entry(root,width=24)
code_text.grid(row=0, column=1)


# 选择过滤类型
imageFilterEnum = StringVar()
combobox = ttk.Combobox(root, 
                        textvariable=imageFilterEnum,
                        state="readonly") # 下拉框
combobox['values'] = [member.name for member in image_.ImageFilterEnum]
combobox.current(0) # 选择默认值
# 定义一个函数，用于处理选择改变事件
def handle_selection_change(event):
    selected_option = combobox.get()
    if selected_option:
        selected_enum_value = image_.ImageFilterEnum[selected_option]
        print(f"Selected Enum Value: {selected_enum_value}")
# 绑定选择改变事件到下拉框  
combobox.bind("<<ComboboxSelected>>", handle_selection_change)
combobox.grid(row=1, column=1)



def change_text(entry, new_text): # 替换为你想要设置的新值
    entry.delete(0, END)
    entry.insert(0, new_text)
def filter_image():
   try:
      image_.filter_image(code_text.get(), os.path.dirname(os.path.abspath(__file__)), imageFilterEnum.get())
      messagebox.showinfo("结果", "转换完成")
   except Exception as e:
      messagebox.showerror("转换错误", e)

def choice_image():
   script_dir = os.path.dirname(os.path.abspath(__file__))
   wait_open_image = filedialog.askopenfile(initialdir=script_dir,title="选择待转换图片",filetypes=(("图片文件","*.jpg"),("all files","*.*")),defaultextension=".jpg").name
   print("待转换图片为 {}".format(wait_open_image))
   change_text(code_text, wait_open_image)

choice_image = Button(root, text="选择图片",command=choice_image)
choice_image.grid(row=0, column=2)
button3 = Button(root, text="转换", command=filter_image)
button3.grid(row=2, column=1)


if __name__ == '__main__':
   root.mainloop()