import calendar
import datetime

def show_calendar(year:int, month:int): 
    print(calendar.month(year,month))
    
def today():
    today = datetime.date.today()
    print("今日是{}年{}月{}日".format(today.year,today.month,today.day))
    show_calendar(today.year,today.month)
    try:
        year = int(input("请输入查询年份:"))
        month = int(input("请输入查询月份:"))
        show_calendar(year,month)
    except:
        print("请输入整数")

if __name__ == '__main__':
    today()