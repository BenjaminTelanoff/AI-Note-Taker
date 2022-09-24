#Importing module
import summarize
raw=summarize.fin

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

#Creating labeled containers for summary + three interesting facts
total={}
i=0
#Sorting to according places
for lib in raw.values():
    sort=sorted(lib.values())
    top=[sort[-1]]                   #highest & second highest scoring sentence
    if sort[-2]>=10:
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
    
    
        

    
#Writing the output text file
with open('basic.txt', 'w') as f:
    None
