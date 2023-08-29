# 需求
使用正则表达式查找和替换文本中的特定模式


# 相关知识点

## 拼接字符串

通过`join`方法，输入数组拼接字符串
```PYTHON
data = ["11","22"]
"".join(data)
```

## python3正则表达式

```PYTHON
import re

text = "你好，世界！这是一个示例文本。"

# 搜索匹配的模式
match = re.search(r"示例", text)
if match:
    print("找到匹配的模式：", match.group())

# 查找所有匹配的模式
matches = re.findall(r"[\u4e00-\u9fa5]+", text)
print("找到的中文文本：", matches)

# 替换匹配的模式
new_text = re.sub(r"示例", "例子", text)
print("更新后的文本：", new_text)
```