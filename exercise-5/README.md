# 需求
实现一个简单的计算器，支持基本的加减乘除运算。

# 相关知识点

## eval
`eval()`是Python内置函数之一，用于将字符串作为代码进行求值和执行。

`eval()`函数接受一个字符串参数，将其作为Python表达式进行求值，并返回结果。该函数可以执行任意合法的Python表达式，包括算术运算、函数调用、变量赋值等。

以下是一些示例用法：

```PYTHON
result = eval("2 + 3")  # 求解表达式 2 + 3
print(result)  # 输出结果 5

expression = "5 * 6 - 2"
result = eval(expression)  # 求解表达式 5 * 6 - 2
print(result)  # 输出结果 28

x = 10
y = 5
expression = "x * y"
result = eval(expression)  # 使用变量进行求值
print(result)  # 输出结果 50

def square(x):
    return x * x

expression = "square(4)"
result = eval(expression)  # 调用函数进行求值
print(result)  # 输出结果 16

```