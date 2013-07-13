# Easy Challenge #125 (http://www.reddit.com/r/dailyprogrammer/comments/1e97ob/051313_challenge_125_easy_word_analytics/)
from collections import Counter

import re
symbol_re = re.compile("[^\w\s]")

messages = [
    "Top three most common words: '{0[0][0]}', '{0[1][0]}', '{0[2][0]}'",
    "Top three most common letters: '{0[0][0]}', '{0[1][0]}', '{0[2][0]}'"
]

f = open('MyDocument.txt', 'r')
data = f.read()

def count_words():
	return len(data.split())

def count_letters():
	return len(data)

def count_symbols():
	return len(symbol_re.findall(data))

def top_three_letters():
	letters_clean = data.replace(" ", "")
	letters = Counter(letters_clean)
	return messages[1].format(letters.most_common(3))

def top_three_words():
	words = data.split()
	word_counter = Counter(words)
	return messages[0].format(word_counter.most_common(3))

print str(count_words()) + " words"
print str(count_letters()) + " letters"
print str(count_symbols()) + " symbols"
print top_three_letters()
print top_three_words()
