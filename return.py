def calc_distance(u1,v1,u2,v2):
  return ((u2 - u1) ** 2 + (v2 - v1) ** 2) ** 0.5

x1 = float(input("x1>"))
y1 = float(input("y1>"))
x2 = float(input("x2>"))
y2 = float(input("y2>"))
distance = calc_distance(x1,y1,x2,y2)
print("distance: %.4f"% distance)

def divide(divident,divisor):
  quotient = divident // divisor
  rest = divident % divisor
  return quotient,rest
dive = int(input("被除数＞"))
divo = int(input("除数＞"))
quotient,rest = divide(dive,divo)
print("商：%d,余り：%d,"% (quotient,rest))