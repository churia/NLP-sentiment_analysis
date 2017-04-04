#-*- coding: utf-8 -*-
import re
regex=re.compile(r"(。|！|？|；|\!|\.|\?|\;|\~)+")
comma=re.compile(r"(\,|，)")
f=open('pkuseg.txt')
array=[]
for line in f:
	if len(line)>80:
		sents=re.split(regex,line)
		for st in sents:
			st=regex.sub("",st)
			if len(st.strip())>0:
				if len(st.strip())>80:
					longs=re.split(comma,st)
					string=""
					i=0
					for l in longs:
						i=i+1
						l=comma.sub(",",l)
						if len(string+l)>100:
							if len(string.strip())>0:
								array.append(string.strip()+" .\n")
								string=l
								if string==",":
									string=""
						else:
							string=string+l
						if i==len(longs) and string.strip() != "":
							array.append(string.strip()+" .\n")
				else:
					array.append(st.strip()+" .\n")
	else:
		array.append(line.strip()+" .\n")
	#array.append('\n')
f.close()

f=open('pkucut.txt','w')
for st in array:
	f.write(st)
f.close()