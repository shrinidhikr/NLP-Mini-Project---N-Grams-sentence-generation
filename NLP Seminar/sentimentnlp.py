import nltk
import csv
import numpy as np
negative = []
with open("words_negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negative.append(row)
print(negative[:10])
positive = []
with open("words_positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        positive.append(row)
print(positive[:10])
def sentiment(text):
    temp = [] 
    text_sent = nltk.sent_tokenize(text)
    for sentence in text_sent:
        n_count = 0
        p_count = 0
        sent_words = nltk.word_tokenize(sentence)
        for word in sent_words:
            word=word.lower()
            for item in positive:
                if(word == item[0]):
                    p_count +=1
            for item in negative:
                if(word == item[0]):
                    n_count +=1
        if(p_count > 0 and p_count > n_count ):
            print( "+ve : " + sentence)
            temp.append(1)
        elif(n_count > 0 and n_count>p_count): 
            print( "-ve : " + sentence)
            temp.append(-1)
        else:
            print ("neutral : " + sentence)
            temp.append(0)
    return sum(temp)
print(sentiment(input("Enter review- ")))
