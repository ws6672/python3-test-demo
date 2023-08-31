
# 需求
使用Python的图像处理库，给一张图片添加滤镜效果。

# 相关知识点

## GUI

### 选择文件时设置类型

```PYTHON
wait_open_image = filedialog.askopenfile(initialdir=script_dir,title="选择待转换图片",filetypes=(("图片文件","*.jpg"),("all files","*.*")),defaultextension=".jpg").name
```

### Combobox

Combobox 是一个Tkinter库中的控件，它是一个组合了文本输入框和下拉框的控件。它允许用户从预定义的选项列表中选择一个选项，或者输入自定义的文本。

Combobox提供了以下常用的功能和特性：

- 显示一个下拉列表，供用户选择选项。
- 允许用户输入自定义的文本，而不仅限于预定义的选项。
- 可以设置默认选择的选项。
- 可以绑定事件，以便在选择改变时执行相应的操作。
- 可以设置样式和外观，以适应应用程序的风格。
  
Combobox通常用于需要提供选项选择的用户界面，如表单输入、设置菜单、过滤器、搜索框等。它是Tkinter中常用的控件之一，提供了一种简单而灵活的方式来处理用户输入和选择。

> 注：要禁止Combobox的输入功能，可以设置state属性为"readonly"。这将使得Combobox控件变为只读模式，用户无法通过键盘输入文本，只能从预定义的选项列表中选择。



#### 示例
1. 选择过滤类型

```PYTHON
imageFilterEnum = StringVar()
combobox = ttk.Combobox(root, textvariable=imageFilterEnum) # 下拉框
combobox['values'] = [member.name for member in image_.ImageFilterEnum]
combobox.current(0) # 选择默认值
```
2. 定义一个函数，用于处理选择改变事件

```PYTHON
def handle_selection_change(event):
    selected_option = combobox.get()
    if selected_option:
        selected_enum_value = image_.ImageFilterEnum[selected_option]
        print(f"Selected Enum Value: {selected_enum_value}")
        
```
3. 绑定选择改变事件到下拉框  

```PYTHON
combobox.bind("<<ComboboxSelected>>", handle_selection_change)
combobox.grid(row=1, column=1)
```


## Pillow

Pillow 是一个Python图像处理库，它是Python Imaging Library（PIL）的一个分支。Pillow库提供了广泛的图像处理功能，能够在Python中打开、操作和保存多种图像格式。
Pillow库可以用于各种图像处理任务，包括调整图像大小、裁剪图像、添加滤镜效果、调整图像亮度和对比度、旋转和翻转图像等。它还支持图像格式的转换，可以将图像从一种格式转换为另一种格式。
Pillow库的主要优点是易于使用和广泛的文档支持。它提供了简单直观的API，使得图像处理任务变得简单和高效。

### 支持的滤镜
Pillow支持各种可以应用于图像的滤镜。Pillow的ImageFilter模块支持的一些滤镜示例包括：

模糊（BLUR）：对图像应用模糊效果。
轮廓（CONTOUR）：找出图像中物体的边缘。
细节（DETAIL）：增强图像的细节。
边缘增强（EDGE_ENHANCE）：增强图像的边缘。
浮雕（EMBOSS）：对图像应用浮雕效果。
锐化（SHARPEN）：锐化图像。生成枚举，枚举值对应ImageFilter.BLUR

使用：
```PYTHON
from enum import Enum, auto

from PIL import Image,ImageFilter

class ImageFilterEnum(Enum):
    BLUR = auto() # 模糊
    CONTOUR = auto() # 轮廓
    DETAIL = auto() # 细节
    EDGE_ENHANCE = auto() # 边缘增强
    EMBOSS = auto() # 浮雕
    SHARPEN = auto() # 锐化

    @staticmethod
    def get_by_str(str):
        result = ImageFilterEnum.BLUR
        for member in ImageFilterEnum:
            if member.name == str:
                result = member
                break
        return result.to_image_filter()
    
    def to_image_filter(self):
        if self == ImageFilterEnum.BLUR:
            return ImageFilter.BLUR
        elif self == ImageFilterEnum.CONTOUR:
            return ImageFilter.CONTOUR
        elif self == ImageFilterEnum.DETAIL:
            return ImageFilter.DETAIL
        elif self == ImageFilterEnum.EDGE_ENHANCE:
            return ImageFilter.EDGE_ENHANCE
        elif self == ImageFilterEnum.EMBOSS:
            return ImageFilter.EMBOSS
        elif self == ImageFilterEnum.SHARPEN:
            return ImageFilter.SHARPEN
```


### 使用滤镜处理图片

```python
import os
from enum import Enum, auto

from PIL import Image,ImageFilter

@staticmethod
def filter_image(src_file_path,output_path,filter_type):
    if not output_path:
        output_path = os.path.dirname(os.path.abspath(__file__))
    # 打开图片
    img = Image.open(src_file_path)
    # 设置过滤
    img = img.filter(ImageFilterEnum.get_by_str(filter_type))
    # 保存图片
    img.save(os.path.join(output_path,re_generator_name(src_file_path)))


@staticmethod
def re_generator_name(file_path:str)->str:
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1]
    name = os.path.splitext(file_name)[0]
    return "{}_解析{}".format(name,file_extension)
```

