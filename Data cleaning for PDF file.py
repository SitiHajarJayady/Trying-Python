from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import PyPDF2 as p2
#import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
#from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

stemmer=PorterStemmer()



PDFfiles= open("a state of art techniques on machine learning algorithms. a perspective of supervised learning approach in data classfication.pdf",'rb') # open the pdf file wnated to extract

pdfread= p2.PdfFileReader(PDFfiles) #created pdf reader



#x=pdfread.getPage(0)
#print(x.extractText())



num_pages = pdfread.getNumPages()
count= 0
text= ""
while count<num_pages:
   pageinfo= pdfread.getPage(count)
   count+=1
   text+=pageinfo.extractText()
   print(text)
  
if text != "":
    text=text

text=text.lower()    #convert text to lowercase
print(text)

text= re.sub("(\\d|\\W)+"," ", text)  #remove numbers
print(text)

text=text.strip()  #remove white spaces
print(text)

tokens = word_tokenize(text)  #tokenize, before remove punctutations so that don't is preserved for punctuation
print(tokens)

punctuations = ['(',')',';',':','[',']',',','-','@','$','&','.','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
stop_words = stopwords.words('english')
#print(stop_words)

text = [word for word in tokens if not word in stop_words and not word in punctuations] #remove punctuations and stop words //not words
print(text)



lemmatizer=WordNetLemmatizer()
for word in text :
   lemmatizer.lemmatize(word)

#print(text)

#text_tokens= word_tokenize(x)

#print(text_tokens)
