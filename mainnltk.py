import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize # from the library nltk we import the module tokenize which has the 
#required functions to tokenize our text
from nltk.corpus import stopwords  #importing the stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt',encoding='utf-8').read()   # We read the contents from the file, encoding used as 
#most of the stuff on the net is encoded in that format.

lowercase = text.lower()
#we convert the text into lowercase as lowercase and uppercase tend to enhibit different emotions.

cleaned_text = lowercase.translate(str.maketrans("","",string.punctuation))
#Now we need to remove the unecessary punctuation marks.
#For that we use the above line where we translate the given text into the reuqired format.
#String.punctuation contains all the punctuations that are to be deleted from the text.

tokenized_words = word_tokenize(cleaned_text,"english")

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:    #extracting each line from the file
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()   #replacing newlines and other stuff
        word,emotion = clear_line.split(":")     #seperately storing the required variables
        if word in final_words:                  #if word in final words
            emotion_list.append(emotion)

w = Counter(emotion_list)   #to count the number of times a particular emotion has occured

def sentiment_analysis(s_text):
    score = SentimentIntensityAnalyzer().polarity_scores(s_text)
    print(score)
    neg_v = score["neg"]
    pos_v = score["pos"]
    if(neg_v>pos_v):
        print("Negative Sentiment")
    elif(pos_v>neg_v):
        print("Positive Sentiment")
    else:
        print("Neutral Statement")

sentiment_analysis(cleaned_text)

fig,axl = plt.subplots()
axl.bar(w.keys(),w.values())    #making a bar graph
fig.autofmt_xdate()             #automatically tilting x axis names
plt.savefig('graph.png')
plt.show()





