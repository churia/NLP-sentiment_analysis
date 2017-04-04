#-*- coding: utf-8 -*-
import re
regex=re.compile(r"(。#PU|！#PU|？#PU|；#PU|\!#PU|\.#PU|\?#PU|\;#PU|\~#PU|，#PU|\,#PU|（#PU [0-9]+#CD ）#PU|[0-9]+#CD ）#PU|[0-9]+#CD \)#PU|[0-9]#CD 、#PU)")
f=open('testpos.txt')
wf=open('TestPosCut.txt','w')
array=[]
for line in f:
	if str(line.strip())>0:
		sentence=line.split("|")
		wf.write(sentence[0].replace("#CD ","").replace("#OD ","").replace("#NT ","").replace("#NN ","")+"|\n")
		sents=re.split(regex,sentence[1])
		for st in sents:
			st=regex.sub("",st)
			if len(st.strip())>0:
				array.append(st.strip())
		array.append('\n')
		for ele in array:
			wf.write(ele+"\n")
		array=[]
f.close()

wf.close()