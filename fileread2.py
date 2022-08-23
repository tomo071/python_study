textfile="result.txt"
f=open(textfile,"r")
for line in f:
  line = f.readline()
  line = line.rstrip("\n")
  print(line)
f.close