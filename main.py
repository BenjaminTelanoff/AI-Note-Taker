from bs4 import BeautifulSoup
with open('sec1.html', 'r') as html_file:
    content = html_file.read()
    real_pars=[]
    soup = BeautifulSoup(content, 'lxml')
    pars_html=soup.find_all('p')
    
    for par in pars_html:
        if len(par)>=340:
            real_pars.append(par)
    print(real_pars)