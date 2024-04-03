import liwc
import unicodedata
from functools import reduce

parse, category_names = liwc.load_token_parser("LIWC2007_Portugues_win.dic")

file = open("demofile.txt", "r", encoding="utf8")
text_original = file.read()

file2 = open("demofile2.txt", "r", encoding="utf8")
text_original2 = file2.read()

def remove_non_ascii_normalized(text):
    normalized = unicodedata.normalize('NFD', text)
    return normalized.encode('ascii', 'ignore').decode('utf-8')

def text_cleaning(text):
    # Definindo a tabela de tradução para substituir os caracteres por espaços
    translation_table = str.maketrans({".": " ", ",": " ", ";": " ", ":": " ",
                                       "(": " ", ")": " ", "[": " ", "]": " ",
                                       "{": " ", "}": " ", '"': " ", "'": " ",
                                       "!": " ", "?": " ", "-": " ", "_": " ",
                                       "+": " ", "=": " ", "*": " ", "/": " ",
                                       "\\": " ", "|": " ", "@": " ", "#": " ",
                                       "$": " ", "%": " ", "&": " ", "^": " ",
                                       "~": " ", "`": " ", "<": " ", ">": " ",
                                       "´": " ", "¨": " ", "ª": " ", "º": " "})
    # Aplicando a tradução na string
    cleaned_text = text.translate(translation_table)
    
    return cleaned_text

def text_lowercasing(text):
    text = text.lower()
    return text

def text_tokenization(text):
    text = text.split()
    return text

def text_liwc(text):
    res = list(map(lambda word: list(parse(word)), text))
    return res

def swear_count(res):
    count = sum(map(lambda word: word.count('swear'), res))
    return count

def anx_count(res):
    count = sum(map(lambda word: word.count('anx'), res))
    return count
 
def posemo_count(res):
    count = sum(map(lambda word: word.count('posemo'), res))
    percentage = (count / len(res)) * 100
    return percentage


    

def negemo_count(res):
    count = sum(map(lambda word: word.count('negemo'), res))
    percentage = (count / len(res)) * 100
    return percentage

def text_sentiment(text_original):
    text = remove_non_ascii_normalized(text_original)
    text = text_cleaning(text)
    text = text_lowercasing(text)   
    text = text_tokenization(text)
    res = text_liwc(text)

    print('Quantidade de palavras:', len(res))
    print('Quantidade de palavras ofensivas:', swear_count(res))
    print('Quantidade de palavras ansiosas: ', anx_count(res))
    print(f'Tom geral positivo: {posemo_count(res):.2f} %')
    print(f'Tom geral negativo: {negemo_count(res):.2f} %')

text_sentiment(text_original)
text_sentiment(text_original2)
