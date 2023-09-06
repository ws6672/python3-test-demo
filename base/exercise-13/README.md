
# 需求
从一个网页中提取所有的链接，并保存到一个文件中。


# 相关知识点

## GUI

### 获取tkinter.Entry的输入框文本
```PYTHON
code_text = Entry(root,width=48)
code_text.grid(row=0, column=1)
wait_use_url = code_text.get()

```

### 复制到剪切板
```python
def path_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_path)
```
## BeautifulSoup
BeautifulSoup是一个Python库，用于从HTML或XML文件中提取数据。它提供了一种简单而直观的方式来遍历、搜索和修改解析树。BeautifulSoup可以处理不规范的标记，并修复错误的标记嵌套关系，使得解析过程更加容易。它是一个非常流行的Web抓取工具，常用于网页数据的爬取和处理。

安装
```SH
pip3 install beautifulsoup4
```

使用：

```PYTHON
import requests
from bs4 import BeautifulSoup
response = requests.get(code_text.get())
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        # find_all用于提取标签
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                links.append(href)
```

### 解析器

1. html.parser：是BeautifulSoup库中的一个解析器，用于解析HTML文档（默认安装）

2. lxml：这是一个高性能的解析器，它使用了C语言库来解析HTML和XML文档。它具有解析速度快和容错能力强的特点。

3. html5lib：这是一个纯Python实现的解析器，它以浏览器的方式解析HTML文档。它可以处理各种不规范的HTML代码，并生成一致的解析结果。


