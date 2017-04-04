import re,operator
dele=re.compile(r"[0-9]+")

AspectArray=[]
WordArray=[]
f=open('Words.txt')
for line in f:	
	WordArray.append(line.strip())
f.close()
f=open('Aspects.txt')
for line in f:	
	AspectArray.append(line.strip())
f.close()

AWords={}
AAspects={}
WAspects={}
WWords={}
f=open('PosCut.txt')
for line in f:
 	words=line.strip().split(" ")
 	wlist=[]
 	alist=[]
 	for word in words:
 		if "#NN" in word:
 			if word.replace("#NN","") not in alist:
 				alist.append(word.replace("#NN",""))
 		if "#VA" in word or "#JJ" in word:
 			if word.replace("#VA","").replace("#JJ","") not in wlist:
 				wlist.append(word.replace("#VA","").replace("#JJ",""))
	for word in alist:
		if word in AspectArray:
			if word in AAspects:
				value=AAspects[word]
				for otherword in alist:
					if otherword != word:
						if otherword in value:
							value[otherword]+=1
						else:
							value[otherword]=1
			else:
				AAspects[word]={}
				value=AAspects[word]
				for otherword in alist:
					if otherword != word:
						value[otherword]=1
			if word in AWords:
				value=AWords[word]
				for otherword in wlist:
					if otherword in value:
						value[otherword]+=1
					else:
						value[otherword]=1
			else:
				AWords[word]={}
				value=AWords[word]
				for otherword in wlist:
					value[otherword]=1
	for word in wlist:
		if word in WordArray:
			if word in WAspects:
				value=WAspects[word]
				for otherword in alist:
					if otherword in value:
						value[otherword]+=1
					else:
						value[otherword]=1
			else:
				WAspects[word]={}
				value=WAspects[word]
				for otherword in alist:
					value[otherword]=1
			if word in WWords:
				value=WWords[word]
				for otherword in wlist:
					if otherword != word:
						if otherword in value:
							value[otherword]+=1
						else:
							value[otherword]=1
			else:
				WWords[word]={}
				value=WWords[word]
				for otherword in wlist:
					if otherword != word:
						value[otherword]=1
f.close()

f=open('OneA_MupW.txt','w')
for line in AspectArray:
	key=line.strip()
	if key in AWords:
		f.write(key+": ")
		value= AWords[key]
		sorted_f = sorted(value.iteritems(), key=operator.itemgetter(1),reverse=True)
		i=0
		for item in sorted_f:
			i+=1
			if i>10:
				break
			f.write(item[0]+" ")
		f.write('\n')
f.close()

f=open('OneA_MupA.txt','w')
for line in AspectArray:
	key=line.strip()
	if key in AAspects:
		f.write(key+": ")
		value=AAspects[key]
		sorted_f = sorted(value.iteritems(), key=operator.itemgetter(1),reverse=True)
		i=0
		for item in sorted_f:
			i+=1
			if i>10:
				break
			f.write(item[0]+" ")
		f.write('\n')
f.close()

f=open('OneW_MupA.txt','w')
for line in WordArray:
	key=line.strip()
	if key in WAspects:
		f.write(key+": ")
		value=WAspects[key]
		sorted_f = sorted(value.iteritems(), key=operator.itemgetter(1),reverse=True)
		i=0
		for item in sorted_f:
			i+=1
			if i>10:
				break
			f.write(item[0]+" ")
		f.write('\n')
f.close()

f=open('OneW_MupW.txt','w')
for line in WordArray:
	key=line.strip()
	if key in WWords:
		f.write(key+": ")
		value=WWords[key]	
		sorted_f = sorted(value.iteritems(), key=operator.itemgetter(1),reverse=True)
		i=0
		for item in sorted_f:
			i+=1
			if i>10:
				break
			f.write(item[0]+" ")
		f.write('\n')
f.close()