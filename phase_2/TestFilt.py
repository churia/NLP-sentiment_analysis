#-*- coding: utf-8 -*-
import re
char=re.compile(r"\#[A-Z]+")
f=open('TestPosCut.txt')
filt=[]
for line in f:
	if "|" in line:
		filt.append(line.strip()+'\n')
	elif len(line.strip())>0:
		words=line.strip().split(" ")
		index=0
		flag=0
		for word in words:
			index+=1
			##if "不#AD" in word:
			##	if index < len(words):
			##		if "#VA" in words[index] or "#JJ" in words[index]:
			##			filt.append(word.replace("#AD","")+" ")
			##			flag=1
			if "不" in word or "没有" in word or "还好" in word:
				filt.append(char.sub("",word)+" ")
				flag=1
			if '#NN' in word or '#VA' in word or '#JJ' in word:
				word=char.sub("",word)
				filt.append(word+" ")
				flag=1
		if flag==1:
			filt.append('\n')
		if line=='\n':
			filt.append(line)
f.close()

f=open('TestFilt.txt','w')
for line in filt:
	f.write(line)
f.close()