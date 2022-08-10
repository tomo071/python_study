
a=int(input("a"))
b=int(input("b"))
c=range(a,b)
print(len(c))
print(min(c))
print(max(c))
print(sum(c))
f_name=input("姓")
l_name=input("名")
age=input("年齢")
fullname=[f_name,l_name]
print("".join(fullname)+"さんは"+age+"歳ですね？")