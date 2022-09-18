#Imports for summarizing it using nltk
import scrape
# import nltk
# from nltk.tokenize import RegexpTokenizer, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem.snowball import SnowballStemmer
# import operator
# import matplotlib.pyplot as plt

#Assingning variables based on imports
# stopwords = stopwords.words('english')
# tokenizer = RegexpTokenizer(r'\w+')
# stemmer = SnowballStemmer('english')
raw=scrape.fin

for value in raw:
    if value.startswith('SUBSECTION')==True:  
        if inSubsec==True:
            None
        else:
            inSubsec=True


