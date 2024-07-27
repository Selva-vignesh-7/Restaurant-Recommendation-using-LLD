#import logging

from gensim.models import LdaModel
from gensim import corpora
import nltk
from nltk.stem.wordnet import WordNetLemmatizer


class Predict():
    def __init__(self):
        dictionary_path = "models/dictionary.dict"
        lda_model_path = "models/lda_model_50_topics.lda"
        self.dictionary = corpora.Dictionary.load(dictionary_path)
        self.lda = LdaModel.load(lda_model_path)

    def load_stopwords(self):
        stopwords = {}
        with open('stopwords.txt', 'rU') as f:
            for line in f:
                stopwords[line.strip()] = 1
        return stopwords

    def extract_lemmatized_nouns(self, new_review):
        stopwords = self.load_stopwords()
        #print(stopwords)
        #ex {'a': 1, "a's": 1, 'able': 1, 'about': 1,
        words = []
        #we divide a given text into different lines by using the function sent_tokenize.
        sentences = nltk.sent_tokenize(new_review.lower())
        #print(sentences)
        for sentence in sentences:
            #We tokenize the words using word_tokenize function available as part of nltk.
            tokens = nltk.word_tokenize(sentence)
            # Word tokenizers is used to find the words
            # and punctuation in a string

            # removing stop words from wordList

            text = [word for word in tokens if word not in stopwords]
            # Using a Tagger. Which is part-of-speech


            tagged_text = nltk.pos_tag(text)

            for word, tag in tagged_text:
                words.append({"word": word, "pos": tag})
            #print(words)

        lem = WordNetLemmatizer()
        #We use NLTK’s Wordnet to find the meanings of words, synonyms, antonyms, and more. 
        #In addition, we use WordNetLemmatizer to get the root word.
        nouns = []
        c=0
        for word in words:
            if word["pos"] in ["NN", "NNS"]:
                nouns.append(lem.lemmatize(word["word"]))
                #print(lem.lemmatize(word["word"]))

                #c=c+1

        #print(nouns)
        return nouns

        


    def run(self, new_review):
        nouns = self.extract_lemmatized_nouns(new_review)


        #above line cleas the text
        #print(nouns)
        #print(self.dictionary(nouns))
        new_review_bow = self.dictionary.doc2bow(nouns) 
        #Convert document (a list of words) into the bag-of-words format = list of (token_id, token_count) 2-tuples
        #print(new_review_bow[0])
        #print(new_review_bow)
        #bag-of-word (BoW) model. In this approach, each document is basically represented by a vector 
        # containing the frequency count of every word in the dictionary.
        #for i,val in new_review_bow:
         #   print(i,val)
        #print("new_review_bow = ", new_review_bow)
        new_review_lda = self.lda[new_review_bow]
        return (new_review_lda)


def main(new_review):
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    predict = Predict()
    x=predict.run(new_review)
    return (x)

if __name__ == '__main__':
    main()


