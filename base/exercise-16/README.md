
# 需求
使用Python连接到数据库并执行查询操作。

# 相关知识点

## sqlite3

sqlite3 是 Python 中的一个内置模块，用于操作 SQLite 数据库。SQLite 是一种轻量级的嵌入式数据库引擎，可以在本地文件中存储和管理数据。

以下是一些常用的 sqlite3 模块的用法示例：

```python
import sqlite3
# 连接到数据库，如果不存在则创建
conn = sqlite3.connect('mydatabase.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# 插入数据
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Alice', 25))
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Bob', 30))

# 提交事务
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 更新数据
cursor.execute("UPDATE employees SET age = ? WHERE name = ?", (26, 'Alice'))
conn.commit()

# 删除数据
cursor.execute("DELETE FROM employees WHERE name = ?", ('Bob',))
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
```