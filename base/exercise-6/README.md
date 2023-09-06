# 需求
实现一个简单的日历应用，可以显示指定年份和月份的日历。

# 相关知识点

## 输出占位符替换


1. 使用`format`方法
```PYTHON
print("今日是{}年{}月{}日".format(today.year,today.month,today.day))
```

2. 使用`f-string`进行占位符替换（仅适用于Python 3.6及以上版本）：
```PYTHON
name = "Alice"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)

```

## calendar

calendar 是Python的内置模块，提供了一些用于处理日期和时间的函数和类。以下是calendar模块的一些常用函数和类的详细描述：

- calendar.month(year, month, w=0, l=0): 返回一个多行字符串，表示指定年份和月份的日历。参数w和l用于指定每个日期的宽度和每周的行数。
- calendar.monthcalendar(year, month): 返回一个嵌套列表，表示指定年份和月份的日历。每个子列表代表一个星期，以整数表示日期。如果某个日期不在指定的月份范围内，则使用0表示。
- calendar.calendar(year, w=2, l=1, c=6): 返回一个多行字符串，表示指定年份的整个日历。参数w、l和c用于指定每个日期的宽度、每周的行数和每个月份之间的间距。
- calendar.weekday(year, month, day): 返回指定日期的星期几，星期一为0，星期日为6。
- calendar.isleap(year): 检查指定年份是否为闰年，是则返回True，否则返回False。
- calendar.leapdays(y1, y2): 返回两个年份之间的闰年数。
- calendar.month_name: 包含一个列表，存储了每个月份的名称。
- calendar.day_name: 包含一个列表，存储了每个星期几的名称。

以上是calendar模块的一些常用函数和类的用法。您以根据需要选择适合的函数或类来处理日期和时间相关的操作。

## datetime

datetime是Python标准库中的一个模块，提供了用于处理日期和时间的类和函数。以下是datetime模块的一些常用类和函数的用法：

1. datetime.datetime类：表示日期和时间的对象，包含年、月、日、时、分、秒和微秒等信息。
```PYTHON
   import datetime

   # 创建一个表示当前日期和时间的datetime对象
   now = datetime.datetime.now()

   # 获取年份、月份、日期、时、分、秒和微秒
   year = now.year
   month = now.month
   day = now.day
   hour = now.hour
   minute = now.minute
   second = now.second
   microsecond = now.microsecond

   # 打印当前日期和时间
   print(now)

```

2. datetime.date类：表示日期的对象，包含年、月、日等信息。
```PYTHON
   import datetime

   # 创建一个表示指定日期的date对象
   date = datetime.date(2022, 9, 6)

   # 获取年份、月份和日期
   year = date.year
   month = date.month
   day = date.day

   # 打印日期
   print(date)

```

3. datetime.time类：表示时间的对象，包含时、分、秒和微秒等信息。
```PYTHON
   import datetime

   # 创建一个表示指定时间的time对象
   time = datetime.time(12, 30, 45)

   # 获取时、分、秒和微秒
   hour = time.hour
   minute = time.minute
   second = time.second
   microsecond = time.microsecond

   # 打印时间
   print(time)

```

4. datetime.timedelta类：表示时间间隔的对象，可以用于进行日期和时间的加减运算。
```PYTHON
   import datetime

   # 创建一个表示1天的时间间隔对象
   one_day = datetime.timedelta(days=1)

   # 获取当前日期
   today = datetime.date.today()

   # 计算明天的日期
   tomorrow = today + one_day

   # 打印明天的日期
   print(tomorrow)

```
