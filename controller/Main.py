from model import SpecialTokenManipulator, StringReader


print(SpecialTokenManipulator.show_answers((StringReader.clean_text(open("./resources/teste.txt", "r", encoding="utf8")))))
