f=open('ans.txt')
wf=open('finalAns.txt',"w")
i=0
pos=[]
neg=[]
none=[]
whole=0
for line in f:
	if "|" in line:
		if i>0:
			if len(pos)>len(neg):
				whole=1
			elif len(pos)<=len(neg):
				whole=2
			if len(pos)==0 and len(neg)==0:
				neg=none
			wf.write(str(i)+'\n')
			for p in pos:
				wf.write(p+" ")
			wf.write("\n")
			for n in neg:
				wf.write(n+" ")
			wf.write("\n"+str(whole)+"\n")
			
			pos=[]
			neg=[]
			none=[]
			whole=0
		i+=1
	else:
		words=line.strip().split(" ")
		if int(words[1])>0:
			pos.append(words[0])
		elif int(words[1])<0:
			neg.append(words[0])
		else:
			none.append(words[0])
if len(pos)>len(neg):
	whole=1
elif len(pos)<=len(neg):
	whole=2
if len(pos)==0 and len(neg)==0:
	neg=none
wf.write(str(i)+'\n')
for p in pos:
	wf.write(p+" ")
wf.write("\n")
for n in neg:
	wf.write(n+" ")
wf.write("\n"+str(whole)+"\n")
f.close()
wf.close()