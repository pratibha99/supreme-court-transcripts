import sys
import codecs
import nltk
import pandas as pd
import re
nltk.download('punkt')

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

from os import listdir
from os.path import isfile, join
inputPath = "textfiles/" ##CHANGE IF NECESSARY

onlyfiles = [f for f in listdir(inputPath) if isfile(join(inputPath, f))]

print(len(onlyfiles))
df = pd.DataFrame(columns=['titles', 'words', 'frequencies'])
for filename in onlyfiles:
    if (".txt" in filename):
        fp = codecs.open("textfiles/" + filename, 'r', 'utf-8')
        words = nltk.word_tokenize(fp.read())

        # Remove single-character tokens (mostly punctuation)


        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

        # Stemming words seems to make matters worse, disabled
        # stemmer = nltk.stem.snowball.SnowballStemmer('german')
        # words = [stemmer.stem(word) for word in words]

        # Remove stopwords
        words = [word for word in words if word not in stop_words]


        #remove punctuation
        words = [re.sub(r'[^\w\s]','', word) for word in words]

        words = [word for word in words if len(word) > 2]

        # Calculate frequency distribution
        fdist = nltk.FreqDist(words)

        title = filename[:-8]
        # Output top 50 words

        for word, frequency in fdist.most_common(50):
            df = df.append({'titles': title, 'words': word, 'frequencies': frequency}, ignore_index=True)

df.to_csv("frequencies.csv")
print(len(df))
