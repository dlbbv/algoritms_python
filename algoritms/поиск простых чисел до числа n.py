import sys

def new_text(text):
    for slovo in text:
        if all(c.isalpha() for c in slovo) and len([c for c in slovo if c in uc_letters]) == 1:
            print(slovo)

uc_letters = [chr(i) for i in range(sys.maxunicode) if chr(i).isupper()]
text = ['агент007', 'ГТО', 'Мама', 'гриБ', 'авТо', 'Три богатыря']

new_text(text)