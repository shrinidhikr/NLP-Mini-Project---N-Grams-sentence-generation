from nltk import CFG
from nltk.parse.generate import generate
from nltk import word_tokenize
from nltk.util import ngrams

text = input("Enter the jumbled sentence: \n")
words = word_tokenize(text)
wordlen = len(words)
print(words)

grammar = CFG.fromstring('''S -> NP VP 
PP -> P NP 
NP -> Det N | NP PP 
VP -> V NP | VP PP
Det -> 'a' | 'the' | 'an'
N -> 'dog' | 'cat' | 'doctor' | 'park' | 'apple' | 'bear' | 'man' | 'women' | 'child' | 'telescope' | 'doll' | 'key' | 'door' | 'home'
V -> 'chased' | 'sat' | 'saw' | 'played' | 'went'
P -> 'on' | 'in' | 'for' | 'under' | 'at' | 'to' ''')
#print(grammar.start())
#print(grammar.productions())
f = 0 
for sentence in generate(grammar,depth=wordlen):
	a =' '.join(sentence)
	b = a.split(" ")
	f = 0
	
	for x in b:
		if(x not in words):
			f=1
	
	
	for word in words:
		if(word not in b):
			f=1
	
	if(f==0):
		print("Correct sentence is: ---> %s"%a)

