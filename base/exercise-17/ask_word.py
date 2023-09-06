import os
import sys
import random

script_path = os.path.dirname(os.path.abspath(__file__))
word_dict=[]

def is_number(input_str):
    return input_str.isdigit()

def load_word_list():
    with open(os.path.join(script_path,'word.txt'),'r') as f:
        for line in f:
            word_dict.append(line.strip())


def word_replace(word:str)->str:
    word_len = len(word)
    # 偶数字符替换为下划线
    for i in range(word_len):
        if i!=0 and i % 2 == 0 and i!=word_len-1:
            word = word.replace(word[i], '_')
    return word

def guess():
    os.system('cls')
    word = random.choice(word_dict)
    while True:
        print("单词加密后为:{}".format(word_replace(word)))
        guess_word = input("请输入可能单词：")
        if guess_word == word:
            print("恭喜你,猜对了!")    
            os.system('cls')
            break

def display_interface():
    os.system('cls')
    while True:
        print('-----------------')
        print('1.开始游戏')
        print('2.退出')
        print('-----------------')
        choice = input("输入选项序号(1/2)：")
        if is_number(choice):
            if int(choice) == 1:
                guess()
            elif int(choice) == 2:
                break

if __name__ == '__main__':
    load_word_list()
    display_interface()
    
