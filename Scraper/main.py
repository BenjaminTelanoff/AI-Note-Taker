from bs4 import BeautifulSoup


with open('sec1.html', 'r') as html_file:
    content = html_file.read()
    
    print(content)