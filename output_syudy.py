from multiprocessing.sharedctypes import Value


for i in range(10):
  print("%d,abcdefg"%i)

try:
  x = int(input("Input>"))
except ValueError:
  print("整数を入力してください")
  exit()
print(x)