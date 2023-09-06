from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import os

wait_compression = []
target_folder = ''


root = Tk()
root.title("简易压缩软件")
root.geometry("500x128")


# bg="#87CEFA" 浅蓝色
label = Label(root,text="待压缩数据：", font=('Arial', 12), width=16, height=2)
label.grid(row=0, column=0)

# 输入框
wait_compression_text = Entry(root)
wait_compression_text.grid(row=0, column=1)


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

def get_parent_folder(path:str)->str:
    return path[:path.rfind('/')]

def compress_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # 去除根目录前缀，获取相对路径
            relative_path = os.path.relpath(root, folder_path)
            for file in files:    
                file_path = os.path.join(root, file)
                if not os.path.isdir(file_path):
                    print("压缩文件路径 {}".format(file_path))
                    zip_path = os.path.join(relative_path, file)
                    zipf.write(file_path, zip_path)

            # 嵌套压缩子文件夹
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                compress_folder(dir_path, output_path)

def compress_files(wait_compression, output_path):
    with zipfile.ZipFile(output_path, "w") as zipf:
        for file_path in wait_compression:
            print("压缩文件路径 {}".format(file_path))
            zipf.write(file_path,arcname=os.path.basename(file_path))

def compress_file():
    try:
        folder = filedialog.asksaveasfilename(initialdir=target_folder,title="保存压缩文件",filetypes=(("zip files","*.zip"),("all files","*.*")),defaultextension=".zip")
        if wait_compression.__len__() == 1 & os.path.isdir(wait_compression[0]):
            compress_folder(wait_compression[0], folder)
        else:
            compress_files(wait_compression, folder)
        messagebox.showinfo("结果", "压缩完成")
    except Exception as e:
        messagebox.showerror("压缩错误", e)

# 定义按钮
button = Button(root, text=" 文件... ", command=open_file)
button.grid(row=0, column=2)
button12 = Button(root, text=" 文件夹... ", command=open_folder)
button12.grid(row=0, column=3)

button3 = Button(root, text=" 开始压缩 ", command=compress_file)
button3.grid(row=2, column=1)

if __name__ == '__main__':
   root.mainloop()