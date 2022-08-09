from re import I


i = int(input("数字を入力してください"))
n = i != 0
fiz=0
buz=0
fizbuz=0
for num in range(i):
  print(num)
  if num % 15 == 0 and n:
    print("fizzbuzz")
    fizbuz +=1
  elif num % 3 == 0 and n:
    print("fizz")
    fiz+=1
  elif num % 5 == 0 and n:
    print("buzz")
    buz+=1
  else:
    if i == 0:
      print("0です")
    else:
      print("どちらにもあてはまりません")
fb=str(fizbuz)
fz=str(fiz)
bz=str(buz)
print("結果は")
print("fizzbuzz" + fb)
print("fizz" + fz)
print("buzz" + bz)
