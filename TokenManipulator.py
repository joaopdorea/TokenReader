import liwc
class TokenManipulator:



    @staticmethod
    def text_liwc(text):
        parse, category_names = liwc.load_token_parser("LIWC2007_Portugues_win.dic")
        res = []
        for word in text:
            resp = list(parse(word))
            res.append(resp)
        return res
    
    @staticmethod
    def swear_count(res):
        count = 0
        for word in res:
            for type in word:
                if type == 'swear':
                    count += 1
        return count
    
    @staticmethod
    def anx_count(res):
        count = 0
        for word in res:
            for type in word:
                if type == 'anx':
                    count += 1
        return count
    
    @staticmethod
    def posemo_count(res):
        count = 0
        for word in res:
            for type in word:
                if type == 'posemo':
                    count += 1
        percentage = (count/len(res)) * 100
        return percentage
    
    @staticmethod
    def negemo_count(res):
        count = 0
        for word in res:
            for type in word:
                if type == 'negemo':
                    count += 1
        percentage = (count/len(res)) * 100
        return percentage

    @staticmethod
    def show_answers(text):
        response = TokenManipulator.text_liwc(text)
        print('Quantidade de palavras:', len(response))
        print('Quantidade de palavras ofensivas:', TokenManipulator.swear_count(response))
        print('Quantidade de palavras ansiosas: ', TokenManipulator.anx_count(response))
        print(f'Tom geral positivo: {TokenManipulator.posemo_count(response):.2f} %')
        print(f'Tom geral negativo: {TokenManipulator.negemo_count(response):.2f} %')

        

    

