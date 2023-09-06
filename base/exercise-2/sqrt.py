import math

# ax²+bx+c=y
def calculate_sqrt(a,b,c,y):
   c -=y
#    判别式
   discriminant= b**2+4*a*c
   if discriminant<0:
      return None
   elif discriminant==0:
      return -b/(2*a)
   else:
      return (-b+math.sqrt(discriminant))/(2*a),(-b-math.sqrt(discriminant))/(2*a)

if __name__ == '__main__':
   print(calculate_sqrt(3,-1,3,0))


