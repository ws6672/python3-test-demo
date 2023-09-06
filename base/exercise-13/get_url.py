import requests
import os
import uuid

from tkinter import *
from tkinter import messagebox

from bs4 import BeautifulSoup

result_path=""
root = Tk()
root.title("网页URL提取器")
root.geometry("500x128")

label = Label(root,text="输入URL：", font=('Arial', 12), width=16, height=2)
label.grid(row=0, column=0)
# 输入框
code_text = Entry(root,width=48)
code_text.grid(row=0, column=1)

def path_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_path)

def str_arr_save(lines)->str:
    global result_path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result_path = os.path.join(script_dir,str(uuid.uuid4())+".txt")
    with open(result_path, "w") as f:
        for line in lines:
            f.write(line)
            f.write("\n")
    return result_path

def get_url():
    try:
        response = requests.get(code_text.get())
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                links.append(href)
        str_arr_save(links)
        messagebox.showinfo("结果", "提取完成,保存路径为{}".format(result_path))
        path_to_clipboard()
    except Exception as e:
        messagebox.showerror("提取错误", e)
    
button = Button(root, text=" 提取url", command=get_url)
button.grid(row=1, column=1)

if __name__ == '__main__':
   root.mainloop()