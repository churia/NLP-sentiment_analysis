import re,operator
f=open('nsubj.txt')
NNarray={}
VAarray={}
dele=re.compile(r"[0-9]+")
for line in f:
	line=line.replace("nsubj(","").replace(")","").replace("-","")
	line=dele.sub("",line)
	sents=line.split(", ")
	if sents[1].strip() in NNarray:
		NNarray[sents[1].strip()]+=1
	else:
		NNarray[sents[1].strip()]=1
	if sents[0] in VAarray:
		VAarray[sents[0]]+=1
	else:
		VAarray[sents[0]]=1
f.close()

sorted_f = sorted(NNarray.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('nn','w')
for item in sorted_f:
    f.write(item[0]+" ")
    f.write(str(item[1])+"\n")
f.close()

sorted_f = sorted(VAarray.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('va','w')
for item in sorted_f:
    f.write(item[0]+" ")
    f.write(str(item[1])+"\n")
f.close()



