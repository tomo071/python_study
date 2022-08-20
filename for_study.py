from asyncio import events
import random as rnd
i=int(input("整数を入力"))
even=0
odd=0
for num in range(i):
  number = str(num)
  if num % 2 == 0:
    even+=1
    print(number + "偶数")
  else:
    odd+=1
    print(number + "奇数")
print(rnd.randrange(num))
print("奇数%d回"%odd)
print("偶数%d回"%even)
w=0
while w<10:
  w+=1
  print(w,end="")
print(w)

