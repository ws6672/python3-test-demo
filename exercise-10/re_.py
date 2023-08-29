import os
import re


pattern = r"3\d+"
replacement = "数据敏感"

def read()->[]:
    arr=[]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data.csv')
    with open(file_path,'r') as file:
         for line in file:
             arr.append(line);
    return arr

def match_and_replace(data:str):
    match = re.search(pattern , data)
    if match:
        data = re.sub(pattern, replacement, data)
        print(data)
    else:
        print("数据不匹配：{} ".format(data))


if __name__ == '__main__':
    for str in read():
        match_and_replace(str)
