# find_best_wordle_word.py
# Author : Yasin ETLİ
# Date created: 21/2/2022
# This script finds the mathematically best first choice of words for the wordle game.

from data import list
from collections import Counter

# Remove words containing repeated letters from the list.

repetitive = []
for words in list:
    word_letters = []
    word_letters.extend((words[0], words[1], words[2], words[3], words[4]))
    letter_count_dict = dict(Counter(word_letters))
    for i in letter_count_dict:
        if letter_count_dict[i] > 1:
            repetitive.append(words)

not_rep = []
for element in list:
    if element not in repetitive:
        not_rep.append(element)

# Calculate every letters' frequency in the original list

key_dict = {
 "a":0, "b": 0, "c": 0, "d": 0,"e": 0,"f": 0,"g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
 "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

for word in list:
    for i in key_dict:
        letter_list = [word[0], word[1], word[2], word[3], word[4]]
        for letter in letter_list:
            if letter == i:
                key_dict[i] +=1
print(key_dict)

# Find the sum of the frequencies of the letters in each word in the original list.
# Then create a dictionary containing the words as keys and the total frequency value as values.
# Sort this created dictionary by values.

master_dict = {}
for word in list:
    letter_list_2 = []
    letter_score_2 = []
    letter_list_2.extend((word[0], word[1], word[2], word[3], word[4]))
    for letter in letter_list_2:
        score = key_dict.get(letter, 0)
        letter_score_2.append(score)
    master_dict[word] = sum(letter_score_2)

master = dict(sorted(master_dict.items(), key=lambda item: item[1]))

print(master)

# Find the sum of the frequencies of the letters in each word in the list where the words containing
# repeated letters are eliminated.
# Then create a dictionary containing the words as keys and the total frequency value as values.
# Sort this created dictionary by values.
# The highest valued word in this dictionary will be the best starting word for the game.

last_dict = {}
for word in not_rep:
    letter_list = []
    letter_score = []
    letter_list.extend((word[0], word[1], word[2], word[3], word[4]))
    for letter in letter_list:
        score = key_dict.get(letter, 0)
        letter_score.append(score)
    last_dict[word] = sum(letter_score)

last = dict(sorted(last_dict.items(), key=lambda item: item[1]))

print(last)

# After applying this code to the English 5-letter words list used here, "arose" was found to be the best
# starting word. After choosing "arose" as the first word in the game, it would be logical to find another
# word that does not contain the letters that this word contains, but consists of other letters that are most
# likely to be encountered. Here, words containing the most common (highest frequency) letters were found,
# except for the letters "a", "r", "o", "s", and "e".

second_word_dict = {}
for i in last:
    let_list = []
    let_list.extend((i[0], i[1], i[2], i[3], i[4]))
    if "a" not in let_list and "r"not in let_list and "o" not in let_list \
            and "s" not in let_list and "e" not in let_list:
        second_word_dict[i] = last[i]

print(second_word_dict)

# As a result, after entering "arose" as the first word, the second recommended word
# was found as "unlit" or "until".

