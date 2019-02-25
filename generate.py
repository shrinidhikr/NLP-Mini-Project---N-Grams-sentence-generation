import nltk
import random
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

text="I am suffering from fever with cough and cold since last night. So I can not come to school. Kindly grand me. I will be highly obliged for your this act of kindness. I am sick. Give me leave.I request to state that due to sudden illness I will not be able to attend school as the doctor has advised me to take the required amount of rest. I hope to recover soon and make up for the irregularity in studies occurred. I will return to school as a healthy student and take care that my work and performance do not suffer. I shall be utterly obliged for this. It is kindly stated that due to a sudden illness I will not be able to attend school for a few days. I request you to grant me leave for the days that I will miss. I hope to recover soon and make up for the lost work. I shall return to school as a healthy student and take care that my work or performance does not suffer. I beg to state with due respect that I am not able to come to school tomorrow as I am feeling really drowsy. The doctor has identified low blood sugar level in me and to properly get treatment I need to visit hospital tomorrow. Because of this situation I request you to please grant me leave for a day. I shall be very grateful to you. I have to notify you that I am not in a position to come to school as I am ill for a week and subjected to complete bed rest for three days. On account of my sickness, I request you to kindly grant me leave. I have got severe cholera and due to this I am not able to be at campus for about three days. I want you to kindly grant me leave. I am already having treatment and I hope to recover from this illness soon. I want to inform that I have kidney problem and for the treatment of which I have an appointment with doctor and I have to go to hospital. Kindly grant me leave for a day so that I can get rid of the problem. After going through a medical checkup yesterday, I got to knew about that I am suffering from malaria and my doctor has advised me complete rest for coming ten days, medical reports of my diagnosis are attached with the application for your reference. Hope you will understand my reasons and will grant me leave. I will be obliged for your approval and considerate response. Most humbly and respectfully I beg to say that I am s since last night. so I will be unable to attend my classes. Please grant me leave. I have been sick since yesterday. My doctor has advised me rest for two days. So I cannot attend the school. Please grant me leave. I request respectfully leave since I am suffering from chicken pox.  I am feeling sick since one week due to bloating. I went to doctor for a checkup and tells me I am suffering from food poisoning and strongly recommends me complete bed rest for next week. I am not in the position to attend the class. I would be very thankful to you. With due respect, It is stated that I am down with fever and chest congestion since two days. Therefore, I am unable to come to school. Please grant me leave. I am weak and hence cannot come to school. "

token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)


#Bigram study
print("\n<--------Bigram yield-------->")
mylist = []
mylist = Counter(bigrams)

#print(mylist)

firstwords = []
secondwords = []
countbgrams = []

for i in mylist:
	firstwords.append(i[0])
	secondwords.append(i[1])
	countbgrams.append(mylist[i])

def generate_bigrams(fstring):
	m = 0
	l=[]
	for x in range(0,len(firstwords)):
		if firstwords[x] == fstring:
			if countbgrams[x] > m:
				del l[:]
				m = countbgrams[x]
				l.append(secondwords[x])
			elif countbgrams[x] == m:
				m = countbgrams[x]
				l.append(secondwords[x])
							
	f = random.choice(l)
	print(f, end=" ")
	return f


k= "I" 
f = 0
print(k, end=" ")
while f!= 3:
	k = generate_bigrams(k)
	if k==".":
		f = f+1
print("\n")


#Trigram study
print("\n<--------Trigram yield-------->")
mylist = []
mylist = Counter(trigrams)	

firstwords = []
secondwords = []
thirdwords = []
counttgrams = []

for i in mylist:
	firstwords.append(i[0])
	secondwords.append(i[1])
	thirdwords.append(i[2])
	counttgrams.append(mylist[i])
	
#print(mylist)


def generate_trigrams(fstring,sstring):
	m=0
	l=[]
	for x in range(0,len(firstwords)):
		if firstwords[x]==fstring and secondwords[x]==sstring:
			if counttgrams[x]>m:
				del l[:]
				m = counttgrams[x]
				first = fstring
				sec=secondwords[x]
				third=thirdwords[x]
				l.append(thirdwords[x])
			elif counttgrams[x]==m:
				m = counttgrams[x]
				sec=secondwords[x]
				l.append(thirdwords[x])
	randomno=random.randint(0,len(l)-1)
	third=l[randomno]
	print(sec, end=" ")
	return sec,third		

if __name__ == "__main__":
	l2="." 
	l3="I"
	f = 0 
	#print(l3)
	while f!= 3:
		l2,l3= generate_trigrams(l2,l3)
		if l3==".":
			f = f+1
	print(".", end=" ")

print("\n")
# Fourgram study
print("\n<--------Fourgram yield-------->")
mylist = []
mylist = Counter(fourgrams)	

firstwords = []
secondwords = []
thirdwords = []
fourthwords = []
countfgrams = []

for i in mylist:
	firstwords.append(i[0])
	secondwords.append(i[1])
	thirdwords.append(i[2])
	fourthwords.append(i[3])
	countfgrams.append(mylist[i])
	
#print(mylist)


def generate_fourgrams(fstring,sstring,tstring):
	m=0
	l=[]
	for x in range(0,len(firstwords)):
		if firstwords[x]==fstring and secondwords[x]==sstring and thirdwords[x]==tstring:
			if countfgrams[x]>m:
				del l[:]
				m = countfgrams[x]
				first = fstring
				l.append(fourthwords[x])
			elif countfgrams[x]==m:
				m = countfgrams[x]
				l.append(fourthwords[x])
	randomno=random.randint(0,len(l)-1)
	fourth=l[randomno]
	print(sstring, end=" ")
	return sstring,tstring,fourth		

if __name__ == "__main__":
	l2="." 
	l3="I"
	f = 0
	choices=["am","have","request"]
	l4=random.choice(choices)
	while f!= 3:
		l2,l3,l4= generate_fourgrams(l2,l3,l4)
		if l4 == ".":
			f = f+1
	print(l3, end=".")
	print("\n")
