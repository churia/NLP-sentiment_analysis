#-*- coding: utf-8 -*-
NNarray={}
VAarray={}
f=open('pkupkunn.txt')
for line in f:
	sts=line.split(" ")
	NNarray[sts[0]]=1
f.close()

array=[]
f=open('nn')
for line in f:
	sts=line.split(" ")
	if sts[0] in NNarray:
		array.append(line)
f.close()

f=open('nnn.txt','w')
for st in array:
	f.write(st)
f.close()

f=open('pkupkuva.txt')
for line in f:
	sts=line.split(" ")
	VAarray[sts[0]]=1
f.close()

array=[]
f=open('va')
for line in f:
	sts=line.split(" ")
	if sts[0] in VAarray:
		array.append(line)
f.close()

f=open('vava.txt','w')
for st in array:
	f.write(st)
f.close()

