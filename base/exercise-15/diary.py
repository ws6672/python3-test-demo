import os
import datetime

DIARY_FILE = 'diary-{}.txt'
script_dir = os.path.dirname(os.path.abspath(__file__))

def is_number(input_str):
    return input_str.isdigit()

def create():
    os.system("cls")
    entry = input ('请输入日志内容:\n')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    file_path = os.path.join(script_dir, DIARY_FILE.format(timestamp))
    with open(file_path, 'a') as f:
        f.write(f'{timestamp}\n{entry}\n\n')
    os.system("cls")
    print('日记已保存！')

def view():
    os.system('cls')
    file_list = [f for f in os.listdir(script_dir) if f.startswith('diary-') and f.endswith('.txt')]
    if not file_list:
        print('没有日记记录!')
    print('---- 日志列表 ----')
    for file in file_list:
        file_path = os.path.join(script_dir, file)
        with open(file_path, 'r') as f:
            content = f.read()
        print(f'--- {file} ---')
        print(content)
        print('-----------------')
    continue_ = input('回车继续!')
    os.system('cls')

if __name__ == '__main__':
    while True:        
        print("欢迎使用日志系统")
        print("1.添加日志")
        print("2.查询日志")
        print("3.退出")
        choice = input("输入选项序号(1/2/3)")
        if is_number(choice):
            if int(choice) == 1:
                create()
            elif int(choice) == 2:
                view()
            elif int(choice) == 3:
                break
        else:
            print("请输入正确的选项序号")
            os.system("cls")