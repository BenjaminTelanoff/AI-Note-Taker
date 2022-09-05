from bs4 import BeautifulSoup
import re

# Opening the HTML File. 
with open('sec1.html', 'r') as html_file:
    content = html_file.read()
    
#Lists - Empty
    pargs=[]

#Parsing through the HTML to find instances of desired class - paragraph in this case.
    soup = BeautifulSoup(content, 'html.parser')
    pars_html=soup.find_all('p', {'class': re.compile('TX')})
    i=1
#Collecting instances, un-textified
    for par in pars_html:
        pargs.append(par.text)
#Finding Suitable Instance
    for par in pargs:
        if len(par)>=340:
#Removing Page Count
            par=str(par)
            if 'page' in par:
                x=par.index('page')
                par=par.replace((par[x:x+8]), "")
#Printing Instances
            print(f'PARAGRAPH {i}:  {par}\n\n')
            i+=1
#Removing access data
        else:
            pargs.remove(par)
    