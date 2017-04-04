#-*- coding: utf-8 -*-
senti=[]
string=""
f=open("tmpAns.txt")
for line in f:
	if "|" in line:
		if len(string.strip())>0:
			senti.append(string)
		string=""
		senti.append(line.strip())
	else:
		words=line.strip().split(" ")
		i=0
		j=0
		flag=0
		for word in words:
			if word =="1" or word =="-1" or word =="0":
				if word=="0" and i+1<len(words) and (words[i+1]=="-1" or words[i+1]=="1"):
					i+=1
					flag=1
					continue
				for k in range(j,i):
					if i-j>1 and words[k]=="酒店":
						continue
					if words[k]=="0":
						continue
					string+=words[k]+" "+word+"\n"
				j=i+1
			if flag==0:
				i+=1
if len(string.strip())>0:
	senti.append(string)
f.close()

f=open("Anslist.txt",'w')
for line in senti:
	f.write(line+"\n")
f.close()

