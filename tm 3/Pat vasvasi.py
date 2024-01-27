import re

b = input()
b = re.sub(r' +',' ',b.strip())
b = re.sub(r"\\n","\n",b)

result=''

b=list(b)

finalres=[]
tmp = 0

for i in b:

    if i=='@':
        finalres.append('@')
        tmp+=1

    elif i =='#' and tmp>0:
        tmp-=1

    else:
        finalres.append(i)

for item in finalres:
     result+=item

print('Formatted Text: '+result)