#!/usr/local/bin/python3

from random import sample
from collections import defaultdict


def main():	

	file = open("metamorphosis.txt",'r')
	inputString = file.read()

	wordTable = defaultdict(list)

	inputString = inputString.replace(",", "")
	inputString = inputString.replace("\n", " ")
	inputString = inputString.replace('\"', " ")

	mening = ""

	for x in inputString.split('.'):
		mening = x.split(" ")
		for i in range(0, len(mening)-1):
			wordTable[mening[i]].append(mening[i+1])

	randWord = sample(list(wordTable), 1)

	currentWord = randWord[0]
	newSentence = ""

	while (wordTable[currentWord]):
		nextWord = sample(wordTable[currentWord], 1)[0]
		newSentence = newSentence + " " + nextWord
		currentWord = nextWord
		

	print(newSentence[1:].capitalize() + ".")


if __name__ == '__main__':
	main()
	