import operator

f=open('ctbpos.txt','r')
lines = [line.strip() for line in f]
f.close()
freq={}
va={}
for line in lines:
    words=line.split(" ")
    for word in words:
        if '#NN' in word:
            if word in freq:
                freq[word]= freq[word]+1
            else:
                freq[word]=1
        if '#VA' in word:
            if word in va:
                va[word]= va[word]+1
            else:
                va[word]=1
   
sorted_f = sorted(freq.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('ctbctbnn.txt','w')
for item in sorted_f:
    f.write(item[0].replace("#NN","")+" ")
    f.write(str(item[1])+"\n")
f.close()

sorted_f = sorted(va.iteritems(), key=operator.itemgetter(1),reverse=True)
f=open('ctbctbva.txt','w')
for item in sorted_f:
    f.write(item[0].replace("#VA","")+" ")
    f.write(str(item[1])+"\n")
f.close()