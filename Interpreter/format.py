#Importing module
import numbers
import string
import summarize
raw=summarize.fin
allo=summarize.raw

#This is a tool that will come in handy later (Mickey Mouse Club House)
def too_short(tofacts, lib, facts):
    sents=[]
    for elem in tofacts:
        sent=((list(lib.keys()) [list(lib.values()).index(elem)]))
        sents.append(sent)
    longest_sent=max(sents, key=len)
    sents.remove(longest_sent)
    facts.append(longest_sent[:85])
    facts.append(longest_sent[85:])
    facts.append(sents[0])
    return facts

#Taking out Subsection and Header
sections=[]
for value in allo:
    if value.startswith('SECTION')==True:
        header=(allo[value])
    elif value.startswith('SUBSECTION')==True:
        sections.append(allo[value])
#Creating labeled containers for summary + three interesting facts
summary={}
factList={}
i=0
#Sorting to according places
for lib in raw.values():
    sort=sorted(lib.values())
    top=[sort[-1]]                   #highest & second highest scoring sentence
    a=(list(lib.keys()) [list(lib.values()).index(sort[-1])])
    b=(list(lib.keys()) [list(lib.values()).index(sort[-2])])
    if sort[-2]>=10 and len(a)<100 and len(b)<100:
         top.append(sort[-2])
    facts=[]
    if len(sort)>=5:
        tofacts=[sort[-3], sort[-4], sort[-5]]
        for elem in tofacts:
            facts.append((list(lib.keys()) [list(lib.values()).index(elem)]))
    elif len(sort)>=4:
        tofacts=[sort[-3], sort[-4]]
        too_short(tofacts, lib, facts)
    elif len(sort)>=3:
        if sort[-2] in top:
             top.pop(sort[-2])
        elem=[sort[-2], sort[-3]]
        too_short(elem, lib, facts)
    else:
        if sort[-2] in top:
             top.pop(sort[-2])
        sort[-2]=elem
        sent=(list(lib.keys()) [list(lib.values()).index(elem)])
        l=(len(sent))/3
        facts.append(sent[:l])
        facts.append(sent[l:2*l])
        facts.append(sent[2*l:])
    tippy=[]
    for num in top:
        tippy.append(list(lib.keys()) [list(lib.values()).index(num)])
    
    i+=1
    summary[i]=tippy
    factList[i]=facts
    

# #TESTING
# for num in range(1,len(summary)+1):
#     print(summary[num])
#     print(factList[num])
#     print('\n\n\n')
    
#Writing the output in text file
up=string.ascii_uppercase
three=['i', 'ii', 'iii']
with open('basic.txt', 'w') as f:
    f.write(header + '\n\n\n')
    for num in range (1, len(summary)+1):
        f.write(up[num-1]+'. '+sections[num-1] + '\n')
        f.writelines(summary[num])
        f.write('\n\n')
        

