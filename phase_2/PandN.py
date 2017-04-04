f=open('stdstd.txt')
POSarray=[]
NEGarray=[]
flag=""
for e, line in enumerate(f):	
	if e%2==0:
		if line.strip()=="1":
			flag="p"
		elif line.strip()=="2":
			flag="n"
	else:
		sents=line.split("|")
		if flag=="p":
			POSarray.append(sents[1])
		elif flag=="n":
			NEGarray.append(sents[1])
		flag="o"
f.close()


f=open('POSstd.txt','w')
for st in POSarray:
	f.write(st)
f.close()

f=open('NEGstd.txt','w')
for st in NEGarray:
	f.write(st)
f.close()
