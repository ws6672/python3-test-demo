import sys

def calculate_sum():
    can_sum = True
    sum_number = 0
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            sum_number+=num
        except ValueError:
            can_sum = False
            break
    if can_sum:
        print(sum_number)
    else:
        print("请输入整数参数")

if __name__ == '__main__':
   calculate_sum()