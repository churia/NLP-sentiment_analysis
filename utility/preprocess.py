#-*- coding: utf-8 -*-
import re
#regex=re.compile(r"(。|！|？|；|\!|\.|\?|\;|\~|[0-9]+\)|[0-9]+、)+")
#comma=re.compile(r"(\,|，)")
rm="宾馆反馈"
rubbish=re.compile(r"补充点评 [0-9]+年[0-9]+月[0-9]+日 ：")
f=open('simpTest.txt')
array=[]
for line in f:
	line=rubbish.sub("",line)
	sents=line.split(rm)
	line=sents[0]
	array.append(line.strip())
f.close()

f=open('stdTest.txt','w')
for line in array:
	f.write(line+'\n')
f.close()