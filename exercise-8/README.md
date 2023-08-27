# 需求
读取一个CSV文件，并提取其中的数据

# 相关知识点

## os模块

os.path模块是Python中用于处理文件路径的内置模块。它提供了一组函数和常量，用于执行与文件路径相关的操作，如路径拼接、目录操作、文件名提取等。

### os.path.join()
os.path.join(path1, path2)：用于将多个路径组合成一个完整的路径。它会根据操作系统的规范自动处理路径分隔符。
os.path.abspath(relative_path): 用于获取一个路径的绝对路径。它将相对路径转换为绝对路径
os.path.dirname(file_path): 用于获取一个路径的目录部分。它返回路径中的目录部分，不包括文件名
os.path.basename()：用于获取一个路径的文件名部分。它返回路径中的文件名，不包括目录部分
os.path.exists()：用于检查一个路径是否存在。它返回一个布尔值，如果路径存在则为True，否则为False

### 获取当前文件的所在目录

```PYTHON
import os

# 获取当前文件的所在目录
printA(os.path.dirname(os.path.abspath(__file__)))
```

## with...as
with...as 是Python中用于创建上下文管理器的语法。上下文管理器可以在特定的代码块中管理资源的获取和释放，以确保资源的正确使用和回收。
语法如下：
```PYTHON
with expression as variable:
    # 代码块 在这个语法中，expression 是一个上下文管理器对象，它可以是一个实现了 __enter__() 和 __exit__() 方法的对象。variable 是一个变量名，用于接收上下文管理器返回的值。
```


```PYTHON
with open(file_path,'r') as file
    #   文件操作
```

### 自定义类支持 with...as

要使自定义类支持with...as语法，您需要在类中实现上下文管理器协议，即定义 __enter__() 和 __exit__() 方法。

- __enter__() 方法用于在进入 with 代码块之前执行的操作，并返回一个值，该值将被赋给 as 子句中的变量。在 __enter__() 方法中，您可以初始化资源或执行其他必要的准备工作。
- __exit__() 方法用于在退出 with 代码块后执行的操作。它接收三个参数：异常类型、异常值和异常追踪。在 __exit__() 方法中，您可以进行资源清理、异常处理等操作。
例如：
```PYTHON
class CustomContextManager:
    def __enter__(self):
        # 在进入 with 代码块之前执行的操作
        # 初始化资源或执行其他准备工作
        print("Entering the context")
        return self  # 可选：返回一个值给 as 子句中的变量

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # 在退出 with 代码块后执行的操作
        # 进行资源清理或异常处理等操作
        print("Exiting the context")

    def some_operation(self):
        # 在 with 代码块内的其他操作
        print("Performing some operation")


# 使用自定义类作为上下文管理器
with CustomContextManager() as manager:
    manager.some_operation()
```