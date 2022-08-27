nums = [5,12,23,43,68,91,105]
x = int(input("整数を入力＞"))
found = False
for n in nums:
  if x == n:
    found = True
    break
if found:
  print("%dが見つかりました!"% x)
else:
  print("%dはありません"% x)
