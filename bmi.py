w=int(input("あなたの体重は？"))
h=int(input("あなたの身長は？"))*0.01
height=h**2
bmi=w/h
bestweight=str(height*22-w)
best=str(height*22)
print("あなたのBMIは"+str(bmi)+"です")
if bmi<18.5:
  print("低体重の傾向があります")
elif 18.5<=bmi and bmi<25.0:
  print("適正体重です")
else:
  print("肥満傾向にあります")
print("あなたの適正体重は"+best+"です")
print("適正体重まで"+bestweight+"kg")
