#Takes any text and changes each non-stopword to be the longest synonym of the word
from PyDictionary import PyDictionary
from nltk.corpus import stopwords
import nltk.tokenize
from sys import argv

stop_words = set(stopwords.words('english'))

def commodiousConfabulation(sentence):
	dictionary = PyDictionary()
	sentence = sentence.lower().split(" ")
	for i in xrange(len(sentence)):
		syn = dictionary.synonym(sentence[i])
		maxLen = -1
		idx = -1
		if sentence[i] not in stop_words:
			if(syn != None):
				for j in xrange(len(syn)):
					if len(syn[j]) > maxLen:
						idx = j
						maxLen = len(syn[j])
				sentence[i] = syn[idx]
	return ' '.join(sentence)


sentence = ""
if(argv[1][-4:] == ".txt"):
	file = open(argv[1], "r")
	sentence = file.read()
	with open(argv[1][:-4]+"CommodiousConfabulation"+argv[1][-4:], "w+") as f:
		f.write(commodiousConfabulation(sentence))
else:
	sentence = argv[1]
	print commodiousConfabulation(sentence)

