# Задание №5
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую
# статистику по исходному файлу:
# Количество символов;
# Количество строк;
# Количество гласных букв;
# Количество согласных букв;
# Количество цифр

import os
import fileinput
import sys

def is_vowel(x):
    glassnie = 'aeiouAEIOU'
    return x in glassnie

with open('Madi.txt', 'r', encoding='utf-8') as file:
    content = file.read()

num_chars = len(content)
num_lines = content.count('\n') + 1
num_vowels = sum(1 for char in content if is_vowel(char))
num_consonants = num_chars - num_vowels
num_digits = sum(1 for char in content if char.isdigit())


with open('ishodii.txt', 'w', encoding='utf-8') as stats_file:
    stats_file.write(f"Количество символов: {num_chars}\n")
    stats_file.write(f"Количество строк: {num_lines}\n")
    stats_file.write(f"Количество гласных букв: {num_vowels}\n")
    stats_file.write(f"Количество согласных букв: {num_consonants}\n")
    stats_file.write(f"Количество цифр: {num_digits}\n")
