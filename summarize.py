#Imports for summarizing it using nltk
import scrape
import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import operator
import matplotlib.pyplot as plt

# #Assingning variables based on imports
stopwords = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer('english')
raw=scrape.fin

#Counters, Lists, and Dictionaries
needSum={}
titles=[]
i=0
titleCount=1

#Organize all sections that need summary
for value in raw:
    if value.startswith('SECTION')==True:
        titles.append(raw[value])
    if value.startswith('SUBSECTION')==True:  
        titles.append(raw[value])
        i+=1
    if i>=1 and value.startswith('PARAGRAPH')==True:
        needSum[i]=raw[value]


for text in needSum.values():
    # tokenize and form nltk objects
    tk = nltk.Text(tokenizer.tokenize(text))
    #remove punctuations and digits and change to lower case
    tk = [w.lower() for w in tk if w.isalpha() and not w.isdigit()]
    #remove stop words and stem the words
    tk = [stemmer.stem(w) for w in tk if w not in stopwords]

    #find word frequencies
    index = nltk.FreqDist(tk)
    #split document into sentences
    sent = sent_tokenize(text)

    #get the title of the text
    tit=(titles[0]+ ' '+ titles[titleCount])
    titleCount+=1
    title = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(tit) if w.isalpha() and w not in stopwords]

    #calculate score for every sentence
    scores = {}
    for sentence in sent:
        #find all words in the sentence
        words = tokenizer.tokenize(sentence)
        words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

        #sum of term frequencies and doc frequencies
        score = 0.0
        titlewords = 0.0
        for word in words:
            score = score + index[word] / (1+index[word])
            if word in title:
                titlewords += 1

        #number of words in sentence / number of those words present in title
        titlewords = 0.1 * titlewords / len(title)
        scores[sentence] = score + titlewords

    print(scores.values())
    print("")
