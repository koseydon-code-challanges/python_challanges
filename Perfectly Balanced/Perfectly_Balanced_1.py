"""
Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false
Optional bonus
Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
Note that balanced_bonus behaves differently than balanced for a few inputs, e.g. "x".
"""

from collections import Counter

def balanced(word):
    balance_check = Counter(word)
    if balance_check["x"] == balance_check["y"] or balance_check == {}:
        print(True)
    else:
        print(False)

def balanced_bonus(word):
    balanced_bonus_check = dict(Counter(word))
    
    list_of_values = [k for k in balanced_bonus_check.values()]
    counter = 0
    check_counter = 0
    while counter < len(list_of_values):
        if list_of_values[0] == list_of_values[counter]:
            check_counter += 1
        counter += 1
    if check_counter == len(list_of_values):
        print(True)
    else:
        print(False)



