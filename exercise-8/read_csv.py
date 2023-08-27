import os

def read_by_open():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data.csv')

    with open(file_path,'r') as file:
        for line in file:
            print(line)

if __name__ == '__main__': 
    read_by_open()