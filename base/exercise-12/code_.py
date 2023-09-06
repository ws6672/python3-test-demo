from tkinter import *
import uuid
code = ""

root = Tk()
root.title("密码生成器")
root.geometry("500x128")


# bg="#87CEFA" 浅蓝色
label = Label(root,text="密码：", font=('Arial', 12), width=16, height=2)
label.grid(row=0, column=0)
# 输入框
code_text = Entry(root,width=64)
code_text.grid(row=1, column=0)


# 定义按钮相关方法
def change_text(entry, new_text): # 替换为你想要设置的新值
    entry.delete(0, END)
    entry.insert(0, new_text)


def generate_password():
    global code
    code = str(uuid.uuid4())
    change_text(code_text, code)

# 定义按钮
button = Button(root, text=" 生成密码... ", command=generate_password)
button.grid(row=2, column=0)

if __name__ == '__main__':
   root.mainloop()