def is_palindrome()->bool:
   data = input("请输入一个字符串，用于判断是否为回文：")
   return data == data[::-1]
if __name__ == '__main__':
   print(is_palindrome())
