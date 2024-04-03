import liwc

parse, category_names = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")

file = open("demofile.txt", "r", encoding="utf8")
text_original = file.read()

file2 = open("demofile2.txt", "r", encoding="utf8")
text_original2 = file2.read()


# replaces special characters with a space
def remove_special_characters(text):
    special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '-', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', '<', '>', ',', '.', '/', '?'
    ]

    clean_text = ''
    for char in text:
        if char in special_characters:
            clean_text += ' '
        else:
            clean_text += char
    return clean_text

# replaces characters with accents with their ASCII standart versions though a dict map
def replace_characters_with_accents(text):
    accent_dict = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'ã': 'a', 'õ': 'o', 'ñ': 'n', 'ç': 'c',
        'Ã': 'A', 'Õ': 'O', 'Ñ': 'N', 'Ç': 'C'
    }

    clean_text = ''
    for char in text:
        if char in accent_dict:
            clean_text += accent_dict[char]
        else:
            clean_text += char
    return clean_text


def to_lowercase(text):
    lowercase_string = []
    for char in text:
        if 'A'<= char <='Z':
            # Range de letras maiúsculas -> 65 a 90
            # Range de letras minúsculas -> 97 a 122
            # 32 números de diferença
            lowercase_string.append(chr(ord(char) + 32))
        else:
            lowercase_string.append(char)

    return ''.join(lowercase_string)

def tokenize_text(text):
    tokens = text.split()
    return tokens

# Parses the tokens using liwc, returning a nested list of sentiments for each token
def parsing_tokens(tokens):
    result = []
    for token in tokens:
        result.append(list(parse(token)))
    return result


def liwc_couting(parsed_text):
    result = {'word_count': '', 'swear_count': '', 'anx_count': '', 'posemo%': '', 'negemo%': '' }

    # Returns interger count value
    result['word_count'] = len(parsed_text)
    result['swear_count'] = sum(1 for item in parsed_text if 'swear' in item)
    result['anx_count'] = sum(1 for item in parsed_text if 'anx' in item)

    # Returns percentage value
    result['posemo%'] = (sum(1 for item in parsed_text if 'posemo' in item) * 100) / result['word_count']
    result['negemo%'] = (sum(1 for item in parsed_text if 'negemo' in item) *100 )/ result['word_count']

    return result


def basic_analysis(text):

    text = remove_special_characters(text)
    text = replace_characters_with_accents(text)
    text = to_lowercase(text)

    tokens = tokenize_text(text)

    liwc_res = parsing_tokens(tokens)

    resp_dict = liwc_couting(liwc_res)
    
    print(f'Total de palavras: {resp_dict["word_count"]}')
    print(f'Palavras ofensivas: {resp_dict["swear_count"]}')
    print(f'Palavras ansiosas: {resp_dict["anx_count"]}')
    print(f'Tom geral positivo: {resp_dict["posemo%"]}')
    print(f'Tom geral negativo: {resp_dict["negemo%"]}')

basic_analysis(text_original)
basic_analysis(text_original2)