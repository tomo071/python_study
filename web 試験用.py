x1 = float(1)
x2 = float(2)
x3 = float(3)
a = float(0)
i = 0
while i == 10000:
  a = a + x1 * x2 / x3
  print("答えは%d"%a)
  x1 += 3
  x2 += 3
  x3 += 3
  i += 1

