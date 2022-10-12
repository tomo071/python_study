a = 0
for i in range(1,30001,3):
  print(i)
  x = i
  x1 = i + 1
  x2 = x1 + 1
  a = x * x1 / x2 
print(a)