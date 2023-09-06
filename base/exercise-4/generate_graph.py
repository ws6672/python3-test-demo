

def  generate_square():
   print("generate square")
   for i in range(10):
     for j in range(10):
       if i==0 or j==0 or i==9 or j==9:
         if j==9:
           print('* \n',end='')
         else:
           print('*',end='')
       else:
         print(' ',end='')
   
def generate_triangle():
   print("generate triangle, input layer:")
   try:
      layer = int(input())
      weight = layer*2-1
      centerIndex = layer-1
      for i in range(layer):
        for j in range(weight):
          if i==layer-1 or j==centerIndex-i or j==centerIndex+i:
            print('*',end='')
          else:
            print(' ',end='')
          if j == weight-1:
            print('\n')

   except ValueError as e:
     print("请输入整数")

if __name__ == '__main__':
   generate_square()
   generate_triangle()