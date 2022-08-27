date = [5, 8, 6, 4, 1, 5, 4]
n = len(date)
for r_end in range(n-1,0,-1):
  for i in range(0,r_end):
    if date[i]>date[i+1]:
      date[i],date[i+1]=date[i+1],date[i]
    print(date)
print(date)
