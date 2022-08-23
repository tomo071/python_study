textfile="result.txt"
f=open(textfile,"r")
lines = f.readlines()
f.close
for line in f:
  line = f.readline()
  line = line.rstrip("\n")
  print(line)
