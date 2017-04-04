import operator
NNarray={}
VAarray={}
f=open('ctbctbnn.txt')
for line in f:
	sents=line.split(" ")
	NNarray[sents[0]]=int(sents[1].strip())
f.close()
f=open('ctbctbva.txt')
for line in f:
	sents=line.split(" ")
	VAarray[sents[0]]=int(sents[1].strip())
f.close()

f=open('nnn.txt')
for line in f:
	sents=line.split(" ")
	if sents[0] in NNarray:
		NNarray[sents[0]]+=int(sents[1].strip())*3
	else:
		NNarray[sents[0]]=int(sents[1].strip())
f.close

f=open('vava.txt')
for line in f:
	sents=line.split(" ")
	if sents[0] in VAarray:
		VAarray[sents[0]]+=int(sents[1].strip())
	else:
		VAarray[sents[0]]=int(sents[1].strip())
f.close

sorted_f = sorted(NNarray.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('nn.txt','w')
for item in sorted_f:
    f.write(item[0]+" ")
    f.write(str(item[1])+"\n")
f.close()

sorted_f = sorted(VAarray.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('va.txt','w')
for item in sorted_f:
    f.write(item[0]+" ")
    f.write(str(item[1])+"\n")
f.close()