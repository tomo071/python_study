import random as rnd
i=int(input("整数を入力"))
for num in range(i):
  number = str(num)
  if num % 2 == 0:
    print(number + "偶数")
  else:
    print(number + "奇数")
print(rnd.randrange(num))