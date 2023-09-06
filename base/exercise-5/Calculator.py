def Calculator():
    try:
        print("启动计算器")
        str = input("请输入一个待计算公式：")
        print(eval(str))
    except NameError:
        print("请输入正确的公式")

if __name__ == '__main__':
    Calculator()