from curses.ascii import isupper
from bs4 import BeautifulSoup
import re

# Opening the HTML File. 
with open('sec.html', 'r') as html_file:
    content = html_file.read()
    
#List, Dictionary, and Counters - Empty
pargs=[]
fin={}
parag_counter=0
sect_counter=0
#Parsing through the HTML to find instances of desired class - paragraph in this case.
soup = BeautifulSoup(content, 'html.parser')
pars_html=soup.find_all(True, {'class':[re.compile('H1'), re.compile('H2'), re.compile('TX')]})


#Collecting instances, un-textified
for par in pars_html:
    pargs.append(par.text)
#Finding Suitable Instance
for par in pargs:
#Removing Page Count and Weird Formating
    par=str(par)
    if 'page' in par:
        x=par.index('page')
        par=par.replace((par[x:x+8]), "")
    if '\xa0' in par:
        par = par.replace(u'\xa0', u' ')

#Differentiating between Titles, Paragraphs, and More

    if par.isupper()==True:
        fin['SECTION']= par
    elif len(par)>1 and len(par)<120:
        sect_counter+=1
        fin[f'SUBSECTION {sect_counter}']= par
    elif len(par)>=120:
        parag_counter+=1
        fin[f'PARAGRAPH {parag_counter}']= par
    elif len(par)<1:
        pargs.remove(par)

#Printing
# for key, value in fin.items():
#     print("{}: {}".format(key, value))
#     print(f'\n')