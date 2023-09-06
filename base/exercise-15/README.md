
# 需求
实现一个简单的命令行日记应用，可以记录和查看日记内容。

# 相关知识点

## datetime
datetime 是 Python 中的一个内置模块，提供了处理日期和时间的功能。通过 datetime 模块，您可以创建日期对象、时间对象和日期时间对象，并进行各种日期时间的计算和操作。

以下是一些常用的 datetime 模块的用法示例：
```PYTHON
import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print("当前日期和时间:", current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print("当前日期:", current_date)

# 创建指定日期和时间的对象
custom_datetime = datetime.datetime(2022, 1, 1, 12, 30, 0)
print("自定义日期和时间:", custom_datetime)

# 获取日期对象的年、月、日
print("年:", custom_datetime.year)
print("月:", custom_datetime.month)
print("日:", custom_datetime.day)

# 获取时间对象的小时、分钟、秒
print("小时:", custom_datetime.hour)
print("分钟:", custom_datetime.minute)
print("秒:", custom_datetime.second)

# 格式化日期时间字符串
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的日期时间:", formatted_datetime)

# 解析字符串为日期时间对象
parsed_datetime = datetime.datetime.strptime("2022-01-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print("解析后的日期时间:", parsed_datetime)

# 日期时间计算和操作
future_datetime = current_datetime + datetime.timedelta(days=7)
print("一周后的日期时间:", future_datetime)

# 比较日期时间
is_future = future_datetime > current_datetime
print("是否在未来:", is_future)

```

## 遍历当前脚本文件夹下的文件

```PYTHON

script_dir = os.path.dirname(os.path.abspath(__file__))
file_list = [f for f in os.listdir(script_dir) if f.startswith('diary-') and f.endswith('.txt')]

```