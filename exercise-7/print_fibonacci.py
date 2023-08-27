def print_fibonacci(n:int):
    a,b = 0,1
    for i in range(n):
        print(a,end=' ')
        a,b = b,a+b

if __name__ == '__main__':
    try:
        n = int(input("请输入数字："))
        print_fibonacci(n)
    except:
        print("请输入整数")