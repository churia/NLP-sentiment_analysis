
array=[]
POSarray={}
NEGarray={}
f=open('Words.txt')
for line in f:	
	array.append(line.strip())
f.close()

f=open('POSpos.txt')
for line in f:
	words=line.split(" ")
	for word in words:
		if '#VA' in word or '#JJ' in word:
			word=word.replace("#VA","").replace("#JJ","")
			if word in array:
				if word in POSarray:
					POSarray[word]= POSarray[word]+1
				else:
					POSarray[word]=1
f.close()

f=open('NEGpos.txt')
for line in f:
	words=line.split(" ")
	for word in words:
		if '#VA' in word or '#JJ' in word:
			word=word.replace("#VA","").replace("#JJ","")
			if word in array:
				if word in NEGarray:
					NEGarray[word]= NEGarray[word]+1
				else:
					NEGarray[word]=1
f.close()

f=open('PNword.txt','w')
for word in array:
	f.write(word+" ")
	p=0
	n=0
	if word in POSarray:
		p=POSarray[word]
	else:
		p=0
	f.write(str(p)+" ")
	if word in NEGarray:
		n=NEGarray[word]
	else:
		n=0
	f.write(str(n)+" ")
	if p==0 and n==0:
		f.write("0")
	elif p-n>0 or n==0:
		f.write("1")
	elif n-p>0 or p==0:
		f.write("-1")
	else:
		f.write("0")
	f.write('\n')
f.close()