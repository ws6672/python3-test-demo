
# 判断为空的几种方式


有下面几种方式判断是否为空
```python
if not a:
    print("None")
if a is None:
    print("None")
if a == None:
    print("None")
```

这三种方式的区别如下

`if not a`是将数据当成boolean计算，有以下几种情况被作为false
1. `False`
2. `None`
3. `0`
4. 空集合 `''`、`[]`、`()`

自定义类如果重写了`__bool__`方法，也会被解析成布尔



`if a == None`是基于`__eq__`方法，如果有重写`__eq__`方法，也可能导致判断出错。另外，该判断会调用 COMPARE_OP，永远比`is`表示的IS_OP要慢。


因此，`if a is None:`是判空的最佳选择。


# 几种配置列表的方法
```python
import sys
# [0] *3 按需分配，不推荐使用。class如此分配，只会复制引用
sys.getsizeof([0] *3) #80=56+8*3
# [0,0,0]使用了 list_extend 字节码方法，resize(3)，底层用了对齐4字节操作，默认分配了8个空间
sys.getsizeof([0,0,0]) #120=56+8*8
# 列表推导式 使用 append字节码，默认4，resize(1) resize(1) resize(1)
sys.getsizeof([0 for - in range(3)]) # 88=56+8*4
```

list分配进行内存对齐的原因：多次分配会产生大量内存分配，底层分配是对齐的

```python
# ~(size_t)3 使用位运算，将上一步的计算结果与 ~(size_t)3 进行按位与操作。~(size_t)3 表示取 3 的补码，然后按位取反。这一步的目的是将计算结果向下舍入到最近的能被 4 整除的值，即将最后两位设置为 0，以确保内存块的对齐。
new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
```

# dis

dis 是一个Python内置模块，用于反汇编Python字节码。它提供了一种查看Python函数或代码块的字节码指令的方式。

要使用 dis 模块，你可以按照以下步骤进行操作：

导入 dis 模块：
```python
import dis
```
定义一个函数或者准备要查看字节码的代码块。

使用 `dis.dis()` 函数来查看字节码指令。将要查看的函数名或代码块作为参数传递给它。例如：

```python
def my_function():
    x = 1
    y = 2
    z = x + y
    print(z)
```

dis.dis(my_function)
这将打印出函数 my_function 的字节码指令。

要注意的是，字节码指令是Python解释器在执行代码时使用的低级指令集。它不是Python代码的源代码，而是在编译过程中生成的中间表示。字节码指令的具体含义和解释可能会根据Python版本和实际代码而有所不同，因此理解字节码指令可能需要对Python的内部工作原理有一定的了解。

# 推导式

## 列表推导式
列表推导式（List Comprehension）是一种简洁的语法，用于创建新的列表，同时可以对现有的列表进行过滤、转换或组合操作。

```python
new_list = [expression for item in iterable if condition]
```
其中，`expression` 是对每个元素进行操作的表达式，`item` 是可迭代对象中的每个元素，`iterable` 是一个可迭代对象（如列表、元组、集合或字符串），`condition` 是一个可选的条件，只有满足条件的元素才会被包含在新列表中。

例如：
```python
# 1. 创建一个包含平方数的新列表
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
# 输出: [1, 4, 9, 16, 25]

# 2. 过滤出大于等于 4 的元素
numbers = [1, 2, 3, 4, 5]
filtered = [x for x in numbers if x >= 4]
# 输出: [4, 5]

# 3.将字符串列表中的每个字符串转换为大写
words = ['hello', 'world', 'codeium']
uppercased = [word.upper() for word in words]
# 输出: ['HELLO', 'WORLD', 'CODEIUM']
```
列表推导式可以根据具体需求进行灵活的定制，使得代码更简洁、易读，并且可以减少循环和条件语句的使用。同时，列表推导式也可以嵌套，允许在一个推导式中使用多个循环和条件语句。

需要注意的是，列表推导式可能在处理大量数据或复杂逻辑时效率不高。在这种情况下，使用生成器表达式或传统的循环方式可能更合适。

## 集合推导式（Set Comprehension）:

集合推导式用于创建新的集合对象。它的语法与列表推导式类似，但使用大括号（`{}`）来表示集合。例如：

```python
numbers = [1, 2, 3, 4, 5]
squares_set = {x**2 for x in numbers}
# 输出: {1, 4, 9, 16, 25}
```

## 字典推导式

字典推导式（Dictionary Comprehension）: 字典推导式用于创建新的字典对象。它的语法类似于列表推导式，但用大括号和冒号（{} 和 :）表示键值对。例如：
```python
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
# 输出: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

