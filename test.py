from re import I


i = int(input("数字を入力してください"))
n = i != 0
if i % 15 == 0 and n:
  print("fizzbuzz")
elif i % 3 == 0 and n:
  print("fizz")
elif i % 5 == 0 and n:
  print("buzz")
else:
  if i == 0:
    print("0です")
  else:
    print("どちらにもあてはまりません")

