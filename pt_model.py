import os
import sys
import spacy

try:
    spacy.load("pt_core_news_sm")
except OSError:
    os.system(f"{sys.executable} -m spacy download pt_core_news_sm")
