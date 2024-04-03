import unicodedata

from TokenManipulator import TokenManipulator
from SpecialTokenManipulator import SpecialTokenManipulator
class StringReader:


    @staticmethod
    def text_lowercasing(text):
        text = text.lower()
        return text

    @staticmethod
    def text_tokenization(text):
        text = text.split()
        return text

    @staticmethod
    def clean_text(file):
        text_original = file.read()
        tokens = StringReader.text_lowercasing(text_original)
        tokens = StringReader.text_tokenization(tokens)
        return tokens




