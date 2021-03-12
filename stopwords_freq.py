# stopwords_freq.py

# Brianna Drew
# March 11, 2021
# ID: #0622446
# Lab #7

# import required libraries and modules
import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist

macbeth_allWords = gutenberg.words('shakespeare-macbeth.txt') # read in words from macbeth
paradise_allWords = gutenberg.words('milton-paradise.txt') # read in words from paradise lost
wonderland_allWords = gutenberg.words('carroll-alice.txt') # read in words from alice in wonderland

macbeth_noStop = [] # empty list to hold words from macbeth excluding stopwords and punctuation characters
paradise_noStop = [] # empty list to hold words from paradise lost excluding stopwords and punctuation characters
wonderland_noStop = [] # empty list to hold words from alice on wonderland excluding stopwords and punctuation characters

# set of common punctuation characters
punctuations = {".", "!", "?", ",", "'", ";", ":", "-", "[", "]", "{", "}", "(", ")", "/", "*", "~",
"<", ">", "`", "^", "_", "|", "#", "$", "%", "+", "=", "&", "@", " "}

# iterate through each word in macbeth, making a new list excluding all the stopwords and punctuation characters
for m in macbeth_allWords:
    if m.lower() not in stopwords.words('english') and m not in punctuations:
        macbeth_noStop.append(m)

# iterate through each word in paradise lost, making a new list excluding all the stopwords and punctuation characters
for p in paradise_allWords:
    if p.lower() not in stopwords.words('english') and p not in punctuations:
        paradise_noStop.append(p)

# iterate through each word in alice in wonderland, making a new list excluding all the stopwords and punctuation characters
for a in wonderland_allWords:
    if a.lower() not in stopwords.words('english') and a not in punctuations:
        wonderland_noStop.append(a)

macbeth_freq = FreqDist(macbeth_noStop) # get word frequencies from the filtered list of words from macbeth
paradise_freq = FreqDist(paradise_noStop) # get word frequencies from the filtered list of words from paradise lost
wonderland_freq = FreqDist(wonderland_noStop) # get word frequencies from the filtered list of words from alice in wonderland

# print the 50 most common words from the filtered list of words from macbeth
print("50 Most Common Words in Macbeth (no stopwords or punctuation):")
print("--------------------------------------------------------------")
print(macbeth_freq.most_common(50), "\n\n")

# print the 50 most common words from the filtered list of words from paradise lost
print("50 Most Common Words in Paradise Lost (no stopwords or punctuation):")
print("--------------------------------------------------------------------")
print(paradise_freq.most_common(50), "\n\n")

# print the 50 most common words from the filtered list of words from alice in wonderland
print("50 Most Common Words in Alice in Wonderland (no stopwords or punctuation):")
print("--------------------------------------------------------------------------")
print(wonderland_freq.most_common(50))