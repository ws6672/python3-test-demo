# 需求
在控制台中绘制一个简单的图形（如正方形、三角形）。


# 相关知识点

## 接收键盘输入
接收键盘输入可以使用Python内置的`input(`)函数。以下是一个示例代码，用于接收用户输入的字符串：


```PYTHON
user_input = input("请输入内容：")  # 接收用户输入
print("您输入的内容是：" + user_input)  # 输出用户输入的内容
```

在运行这段代码时，程序会暂停等待用户输入，并将用户输入的内容存储在user_input变量中。然后，程序会打印出用户输入的内容。

## range函数

`range()`函数在Python中用于生成一个整数序列，可以用来进行循环迭代或创建列表。

`range()`函数可以接受一个、两个或三个参数：

- 当只有一个参数时，range(stop)会生成从0到stop-1的整数序列。
- 当有两个参数时，range(start, stop)会生成从start到stop-1的整数序列。
- 当有三个参数时，range(start, stop, step)会生成从start到stop-1的整数序列，步长为step。


```PYTHON
# 生成从0到4的整数序列
for num in range(5):
    print(num)

# 生成从1到5的整数序列
for num in range(1, 6):
    print(num)

# 生成从0到10的偶数序列
for num in range(0, 11, 2):
    print(num)

# 使用range生成列表
numbers = list(range(1, 6))
print(numbers)
```

`range()`函数生成的整数序列被用于循环迭代或创建列表。