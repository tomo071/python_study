import random as rnd
num = int(input("整数を入力"))
count = 0
random = -1
max = int(input("max"))
if num<max:
  while random != num:
    random = rnd.randrange(max)
    print(random)
    count += 1
  print("%d回目に%dが出ました"% (count,num))
else:
  print("無限ループが発生します")