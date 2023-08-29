from tkinter import *
from tkinter import filedialog
import zipfile
import os
import uuid

wait_compression = []
target_folder = ''


root = Tk()
root.title("简易压缩软件")
root.geometry("500x128")


# bg="#87CEFA" 浅蓝色
label = Label(root,text="待压缩：", font=('Arial', 12), width=16, height=2)
label.grid(row=0, column=0)
label2 = Label(root,text="生成位置：", font=('Arial', 12), width=16, height=2)
label2.grid(row=1, column=0)

# 输入框
wait_compression_text = Entry(root)
wait_compression_text.grid(row=0, column=1)
target_folder_text = Entry(root)
target_folder_text.grid(row=1, column=1)


# 定义按钮相关方法
def change_text(entry, new_text): # 替换为你想要设置的新值
    entry.delete(0, END)
    entry.insert(0, new_text)

def update_compression_target(file_paths):
    global wait_compression
    global target_folder
    wait_compression = file_paths
    target_folder = get_parent_folder(file_paths[0])
    change_text(wait_compression_text, "".join(wait_compression))
    change_text(target_folder_text,target_folder)

def open_file():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        print("选择的文件路径：", file_paths)
        update_compression_target(file_paths)

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("选择的文件夹路径：", folder_path)
        update_compression_target([folder_path])


def save_folder():
    global target_folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("选择的文件夹路径：", folder_path)
        target_folder = get_parent_folder(folder_path)
        change_text(target_folder_text,target_folder)

def get_parent_folder(path:str)->str:
    return path[:path.rfind('/')]

def compress_file():
    if wait_compression.__len__() == 1 & os.path.isdir(wait_compression[0]):
    # todo
        pass
    with zipfile.ZipFile(os.path.join(target_folder,str(uuid.uuid4())+".zip"), "w") as zipf:
        for file_path in wait_compression:
            zipf.write(file_path)

# 定义按钮
button = Button(root, text=" 文件... ", command=open_file)
button.grid(row=0, column=2)
button12 = Button(root, text=" 文件夹... ", command=open_folder)
button12.grid(row=0, column=3)
button2 = Button(root, text=" 选择... ",command=save_folder)
button2.grid(row=1, column=2)

button3 = Button(root, text=" 开始压缩 ", command=compress_file)
button3.grid(row=2, column=1)

if __name__ == '__main__':
   root.mainloop()