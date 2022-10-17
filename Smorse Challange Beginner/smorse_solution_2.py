from collections import Counter

def english_to_morse(english):
    return "".join([morse_translation[char] for char in english])

def balanced(morse):
    return len(morse.replace('-', '')) == len(morse.replace('.', ''))

def is_palindrome(text):
    return text == text[::-1]

def permutations(chars, max_length):
    options = chars
    values = []
    index = -1
    while True:
        index += 1
        if index == len(options):
            break
        if len(options[index]) == max_length:
            values.append(options[index])
        else:
            options.append(options[index] + ".")
            options.append(options[index] + "-")
    return values

def get_all_sequences(morse_lines):
    seq = set()
    for morse in morse_lines:
        l = len(morse)
        if l < 13:
            continue
        for idx in range(0, l - 13): # Should be l - 12
            seq.add(morse[idx:13+idx])
    return seq

with open(r'/Users/denizhasirci/Desktop/Python Works/Smorse Challange Beginner/enable1.txt', 'r') as f:
    words = f.read().strip().split('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ')

morse_translation = dict(zip(alphabet, morse))
english_translation = dict(zip(morse, alphabet))

dict_morse = {english_to_morse(word): word for word in words}
dict_english = {word: english_to_morse(word) for word in words}

morse_lines = [english_to_morse(word) for word in words]
morse_counter = Counter(morse_lines)

sequences_of_thirtheen = get_all_sequences(morse_lines)

print('1: ', [morse_seq for morse_seq in morse_counter if morse_counter[morse_seq] == 13][0])
print('2: ', dict_morse[[morse_seq for morse_seq in morse_counter if '-'*15 in morse_seq][0]])
print('3: ', [word for word, morse in dict_english.items() if len(word) == 21 and balanced(morse) and not word == 'counterdemonstrations'][0])
print('4: ', [word for word, morse in dict_english.items() if len(word) == 13 and is_palindrome(morse)][0])
print('5: ', [permutation for permutation in permutations(['.', '-'], 13) if not permutation in sequences_of_thirtheen and not permutation == '--.---.---.--'])