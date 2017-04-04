import re

num=re.compile(r"[0-9]+")

aspect={}
f=open('Anslist.txt')
wf=open('ans.txt','w')
for line in f:
	if "|" in line:
		if len(aspect)>0:
			for key,value in aspect.items():
				wf.write(key+" "+str(value)+"\n")
				aspect={}
		wf.write(line.strip()+'\n')
	else:
		tmp=num.sub("",line)
		if len(tmp.replace(" ","").strip())>0:
			words=line.strip().split(" ")
			if words[0] in aspect:
				aspect[words[0]]+=int(words[1])
			else:
				aspect[words[0]]=int(words[1])
if len(aspect)>0:
	for key,value in aspect.items():
		wf.write(key+" "+str(value)+"\n")
wf.close()
f.close()