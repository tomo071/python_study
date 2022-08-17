import random as rnd
num=int(input("整数を入力"))
count=0
random=-1
max = 1000
while random != num:
  random = rnd.randrange(max)
  count += 1
print("%d回目に%dが出ました"% (count,num))