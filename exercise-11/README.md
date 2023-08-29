# 需求
实现一个简单的文件压缩工具，将文件或目录压缩成ZIP格式。


# 相关知识点

## tkinter

### 初始化
```PYTHON
# 创建一个Tkinter应用程序的主窗口
root = tk.Tk()
root.title("文本")
root.geometry("500x128")

# 创建小部件

# 运行主事件循环（main event loop）
root.mainloop()
```


### 坐标

在Tkinter中，坐标的单位是像素（pixel）。像素是显示设备上的最小可见点，它们用于确定小部件（widget）的位置和大小。

Tkinter使用以左上角为原点的坐标系统，水平方向向右增加（x），垂直方向向下增加（Y）。坐标值表示小部件相对于其父容器（如窗口或框体）的位置。

例如，如果一个小部件的坐标是(x, y)，那么它的左上角将位于距离父容器的左上角x像素的水平位置和y像素的垂直位置。

> 请注意，Tkinter 还支持其他布局管理器，如pack、grid和place。这些布局管理器可以帮助你更灵活地控制小部件的位置和大小，而不仅仅依赖于坐标。


### 布局管理器
Tkinter提供了三种主要的布局管理器：

Pack布局管理器：pack()方法按照添加的顺序将小部件放置在父容器中。它默认将小部件从上到下垂直排列，也可以通过side参数设置为LEFT、RIGHT、TOP或BOTTOM来改变排列方向。

Grid布局管理器：grid()方法通过行和列的网格布局来放置小部件。你可以使用row和column参数指定小部件所在的行和列，还可以使用rowspan和columnspan参数指定小部件跨越的行数和列数。

Place布局管理器：place()方法允许你以绝对坐标的方式放置小部件。你可以使用x和y参数指定小部件的左上角的位置，并使用anchor参数指定小部件在该位置的对齐方式。

这些布局管理器可以根据你的需求来选择和组合使用。你可以根据小部件的复杂性和布局要求选择最合适的布局管理器。此外，你还可以使用Frame小部件来创建嵌套布局，以实现更复杂的界面布局。

```PYTHON
# 按顺序布局，只支持一个方向
text_entry.pack(side=LEFT)

# 网格布局
label1.grid(row=0, column=0)

```


### filedialog 

filedialog 是Python标准库中的一个模块，它提供了一组用于文件对话框操作的函数。通过该模块，您可以方便地与用户交互选择文件和目录的操作。

filedialog 模块通常与 tkinter（Python的标准GUI库）一起使用，并提供了以下函数：

- filedialog.askopenfilename()：显示一个文件打开对话框，让用户选择一个文件，并返回所选文件的路径。
- filedialog.asksaveasfilename()：显示一个文件保存对话框，让用户选择保存文件的路径和文件名，并返回所选文件的路径。
- filedialog.askopenfilenames()：显示一个文件打开对话框，让用户选择多个文件，并返回所选文件的路径列表。
- filedialog.askdirectory()：显示一个目录选择对话框，让用户选择一个目录，并返回所选目录的路径。

可选参数：
- defaultextension	指定文件的后缀，如果用户输入文件名包含后缀，那么该选项不生效
- filetypes	指定筛选文件类型的下拉菜单选项；选项值是由 2 元祖（类型名，后缀）构成的列表
- initialdir 默认保存目录
- parent 如果不指定该选项，那么对话框默认显示在根窗口上；如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w
- title	指定文件对话框的标题栏文本


这些函数提供了一个标准的、跨平台的界面，让用户可以方便地选择文件或目录。在对话框中，用户可以浏览文件系统、搜索文件、创建新文件夹等。

如果不指定该选项，那么对话框默认显示在根窗口上


## zipfile
zipfile 是Python标准库中的一个模块，用于处理 ZIP 文件。通过 zipfile 模块，您可以创建、读取和提取 ZIP 文件，以及对其中的文件进行压缩和解压缩操作。

zipfile 模块提供了一组类和函数，用于处理 ZIP 文件。以下是一些常用的 zipfile 模块的功能：

ZipFile 类：用于表示 ZIP 文件。您可以使用 ZipFile 类创建、打开和操作 ZIP 文件。它提供了一系列方法，例如 extractall() 用于解压缩所有文件，extract() 用于解压缩单个文件，write() 用于将文件添加到 ZIP 文件中等。

ZipInfo 类：用于表示 ZIP 文件中的单个文件的信息。ZipFile 类的一些方法返回 ZipInfo 对象，您可以使用它来获取文件的名称、压缩信息、时间戳等。


示例：
```PYTHON

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

```