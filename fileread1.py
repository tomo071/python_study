textfile="html1.html"
f=open(textfile,"r")
while True:
  line = f.readline()
  if line == "":
    break
  line = line.rstrip("\n")
  print(line)
f.close