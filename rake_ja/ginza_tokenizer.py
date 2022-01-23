from ginza import token_i
import spacy
from collections import namedtuple

#Morpheme = namedtuple("Morpheme", "surface pos pos_s1 pos_s2 pos_s3 conj form")
Morpheme = namedtuple("Morpheme", "surface i lemma tag pos") # surface には text を格納

class GinzaTokenizer:
    def __init__(self,  model='ja_ginza') :
        self.nlp = spacy.load(model)
    
    def tokenize(self, text) :
        return [m for m in self.__iter_morpheme(text)]
    
    def __iter_morpheme(self, text):
        doc = self.nlp(text)
        for sent in doc.sents :
            for token in sent :
                token_i = token.i
                token_text = token.text
                token_lemma = token.lemma_
                token_tag = token.tag_
                token_pos = token.pos_
                yield Morpheme(token_text, token_i, token_lemma, token_tag, token_pos)