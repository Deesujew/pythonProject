import re
def has_cyrillic(wrd):
    return bool(re.search('[а-яА-Я]', wrd))
dct_en =   {1: "AEIOULNSTR",
            2: "DG",
            3: "BCMP",
            4: "FHVWY",
            5: "K",
            8: "JX",
            10: "QZ"}
dct_ru =    {1: "АВЕИНОРСТ",
             2: "ДКЛМПУ",
             3: "БГЁЬЯ",
             4: "ЙЫ",
             5: "ЖЗХЦЧ",
             8: "ШЭЮ",
             10: "ФЩЪ"}

wrd = input("Введите слово:").upper()

sum=0

if has_cyrillic(wrd):
    for i in wrd:
       for k, v in  dct_ru.items():
           if i in v:
               sum = sum + k
else:
    for i in wrd:
       for k, v in  dct_en.items():
           if i in v:
               sum = sum + k

print(sum)