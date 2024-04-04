import nltk
from nltk.corpus import brown

nltk.download('stopwords')

# generate a list of the 1000 most common words in the brown corpus
# and write them to a file

most_common = brown.words()
most_common = [word.replace("'", "") for word in most_common]
most_common= [word.lower() for word in most_common if word.isalpha()]
most_common = nltk.FreqDist(w.lower() for w in most_common)
most_common = most_common.most_common(600)

with open('most_common_words.txt', 'w') as f:
    for word in most_common:
        f.write(word[0] + '\n')
