import os
import fileinput
import sys
from transliterate import translit
from docx import Document

with open('русскийтекст.txt','r',encoding='utf - 8') as a:
    rus = a.read()
with open('английскийтекст.txt', 'w') as b:
    tranlate = translit(rus, 'ru', 'en')
    b.write(tranlate)

