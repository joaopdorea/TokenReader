import liwc
import unicodedata
from TokenManipulator import TokenManipulator
class SpecialTokenManipulator(TokenManipulator):

    @staticmethod
    def remove_non_ascii_normalized(text):
        normalized = unicodedata.normalize('NFD', text)
        return normalized.encode('ascii', 'ignore').decode('utf-8')
    
    @staticmethod
    def destokenization(list):
        phrase = ""
        for i in range(len(list)):
            if(i != len(list) - 1):
                phrase = phrase + list[i] + " " 
            else:
                phrase = phrase + list[i]
        return phrase



                
    @staticmethod
    def text_cleaning(text):
        for char in text:
            if char == ".":
                text = text.replace(char, "  ")
            elif char == ",":
                text = text.replace(char, "  ")
            elif char == ";":  
                text = text.replace(char, "  ")
            elif char == ":": 
                text = text.replace(char, "  ")
            elif char == "(":
                text = text.replace(char, "  ")
            elif char == ")":
                text = text.replace(char, "  ")
            elif char == "[":
                text = text.replace(char, "  ")
            elif char == "]":
                text = text.replace(char, "  ")
            elif char == "{":
                text = text.replace(char, "  ")
            elif char == "}":
                text = text.replace(char, "  ")
            elif char == '"':
                text = text.replace(char, "  ")
            elif char == "'":
                text = text.replace(char, "  ")
            elif char == "!":
                text = text.replace(char, "  ")
            elif char == "?":
                text = text.replace(char, "  ")
            elif char == "-":
                text = text.replace(char, "  ")
            elif char == "_":
                text = text.replace(char, "  ")
            elif char == "+":
                text = text.replace(char, "  ")
            elif char == "=":
                text = text.replace(char, "  ")
            elif char == "*":
                text = text.replace(char, "  ")
            elif char == "/":
                text = text.replace(char, "  ")
            elif char == "\\":
                text = text.replace(char, "  ")
            elif char == "|":
                text = text.replace(char, "  ")
            elif char == "@":
                text = text.replace(char, "  ")
            elif char == "#":
                text = text.replace(char, "  ")
            elif char == "$":
                text = text.replace(char, "  ")
            elif char == "%":
                text = text.replace(char, "  ")
            elif char == "&":
                text = text.replace(char, "  ")
            elif char == "^":
                text = text.replace(char, "  ")
            elif char == "~":
                text = text.replace(char, "  ")
            elif char == "`":
                text = text.replace(char, "  ")
            elif char == "<":
                text = text.replace(char, "  ")
            elif char == ">":
                text = text.replace(char, "  ")
            elif char == "´":
                text = text.replace(char, "  ")
            elif char == "¨":
                text = text.replace(char, "  ")
            elif char == "ª":
                text = text.replace(char, "  ")
            elif char == "º":
                text = text.replace(char, "  ")
        return text
    
    @staticmethod
    def text_tokenization(text):
        text = text.split()
        return text

    
    @staticmethod
    def show_answers(text):
        text = SpecialTokenManipulator.destokenization(text)
        text = SpecialTokenManipulator.remove_non_ascii_normalized(text)
        text = SpecialTokenManipulator.text_cleaning(text)
        text = SpecialTokenManipulator.text_tokenization(text)
        response = TokenManipulator.text_liwc(text)
        print('Quantidade de palavras:', len(response))
        print('Quantidade de palavras ofensivas:', TokenManipulator.swear_count(response))
        print('Quantidade de palavras ansiosas: ', TokenManipulator.anx_count(response))
        print(f'Tom geral positivo: {TokenManipulator.posemo_count(response):.2f} %')
        print(f'Tom geral negativo: {TokenManipulator.negemo_count(response):.2f} %')

        

    

