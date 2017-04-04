#-*- coding: utf-8 -*-
aspectArray=[]
f=open('Aspects.txt')
for line in f:
	aspectArray.append(line.strip())
f.close()

opinionArray={}
f=open('Words.txt')
for line in f:
	opinionArray[line.strip()]=0
f.close()

aspectExtend={}
f=open('aspExt.txt')
for line in f:
	sents=line.strip().split(":")
	extends=sents[1].strip().split(" ")
	for ext in extends:
		if len(ext.strip())>0:
			aspectExtend[ext.strip()]=sents[0]
f.close()

f=open('TestFilt.txt')
filt=[]
for line in f:
	if "|" in line:
		filt.append(line.strip())
	elif len(line.strip())>0:
		words=line.strip().split(" ")
		string=""
		for word in words:
			if word in aspectArray:
				string+=word+" "
			if word in opinionArray or "不" in word:
				string+=word+" "
			if word in aspectExtend:
				string+=word+" "
		if len(string)>0:
			filt.append(string.strip())
f.close()

f=open('filter.txt','w')
for line in filt:
	f.write(line+'\n')
f.close()

f=open('PNword.txt')
for line in f:
	sents=line.strip().split(" ")
	opinionArray[sents[0]]=int(sents[3])
f.close()

word2asp={}
f=open('word2asp.txt')
for line in f:
	sents=line.strip().split(":")
	opinions=sents[1].strip().split(" ")
	for ext in opinions:
		if len(ext.strip())>0:
			word2asp[ext.strip()]=sents[0]
f.close()

f=open('filter.txt')
aspect=[]
string=""
for line in f:
	if "|" in line:
		if len(string.strip())>0:
			aspect.append(string)
		string=""
		aspect.append(line.strip())
	elif len(line.strip())>0:
		words=line.strip().split(" ")
		flag=0
		t=0
		for word in words:
			if t==0 and word in word2asp:
				string+=word2asp[word]+" "
			if word in opinionArray:
				if "不" in line and "不" not in word:
					string+=str(-opinionArray[word])+" "
				else:
					string+=str(opinionArray[word])+" "
				if opinionArray[word]!=0:
					flag=1
				t=0
			if "没有" in word:
				string+="-1 "
			if word=="问题":
				string+="-1 "
			if word=="还好":
				string+="1 "
			elif word in aspectArray:
				string+=word+" "
				t=1
			if word in aspectExtend:
				string+=aspectExtend[word]+" "
				t=1
		if flag==0:
			if "不" in line:
				string+="-1"
			else:
				string+="0"
		string+="\n"
if len(string.strip())>0:
	aspect.append(string)
f.close()

f=open("tmpAns.txt",'w')
for line in aspect:
	f.write(line+"\n")
f.close()
