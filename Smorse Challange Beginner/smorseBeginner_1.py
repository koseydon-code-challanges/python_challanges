from collections import Counter
import random
import string

codeDict = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}

inputread = open("/Users/denizhasirci/Desktop/Python Works/Smorse Challange Beginner/enable1.txt", "r").read()
replacedN = inputread.replace("\n", " ")

lst3 = replacedN.split(" ")

def smorse(word):
    counter1 = 0
    list1 = []
    list2 = []
    
    while counter1 < len(word):
        list1.append(word[counter1])
        counter1 += 1
        
    else:
        counter2 = 0
        str1 = ""
        while counter2 < len(list1):
            
            if list1[counter2] != " ":
                str1 += codeDict[list1[counter2]]
                counter2 += 1
                
            else:
                list2.append(str1)
                counter2 += 1
                str1 = ""

        else:
            list2.append(str1)

    return list2

def thirteen():
    smorse_list = smorse(replacedN)
    thirteen_dict = dict(Counter(smorse_list))
    print(list(thirteen_dict.keys())[list(thirteen_dict.values()).index(13)])

def fifteen_dashes():
    smorse_list = smorse(replacedN)
    fifteen_dash = "-"*15
    dash_counter = 0

    while dash_counter < len(smorse_list):
        if fifteen_dash in smorse_list[dash_counter]:
            #print(smorse_list[dash_counter])
            print(lst3[dash_counter])
            break
        else:
            dash_counter += 1

def perf_balan():
    balance_counter = 0 

    while balance_counter < len(lst3):


        if len(lst3[balance_counter]) == 21:

            balanced_code = []
            code_plus = ""
            
            code_plus = lst3[balance_counter]
            
            balanced_code = smorse(code_plus)
            print(balanced_code)
            
            number_char = dict(Counter(balanced_code[0]))

            #print(lst3[balance_counter]),
            #print(number_char["."])
            #print(number_char["-"])

            if number_char["."] == number_char["-"] and code_plus != "counterdemonstrations":
                print(number_char)
                print(lst3[balance_counter])
                break
            balance_counter += 1

        else:
            balance_counter += 1

def palin_13():
    palin_counter = 0
    codeList = smorse(replacedN)

    while palin_counter < len(codeList):

        if len(lst3[palin_counter]) == 13:

            if codeList[palin_counter] == codeList[palin_counter][::-1]:
                print(lst3[palin_counter])
                break
            else:
                palin_counter += 1
        else:
            palin_counter += 1

## Generate a random string of specific characters 
def randString(length=13):
    #put your letters in the following string
    your_letters='.-'
    return ''.join((random.choice(your_letters) for i in range(length)))

def only_13():
    counter1 = 0
    counter2 = 0
    bigger_thirteen = []
    only_thirteen_list = []
    random_seq = ""
    codeList = smorse(replacedN)

    while counter1 < len(codeList):
        if len(codeList[counter1]) > 12:
            bigger_thirteen.append(codeList[counter1])
            counter1 += 1
        else:
            counter1 += 1
            
    else:
        while len(only_thirteen_list) < 5:
            random_seq = randString()        
            while counter2 < len(bigger_thirteen):
                if random_seq not in bigger_thirteen[counter2]:
                    counter2 += 1
                else:
                    random_seq = randString() 
            else:
                only_thirteen_list.append(random_seq)
                          
        else:
            print(only_thirteen_list)
            
        
#uinput = input("Please enter the word yopu want do code: ")
#fifteen_dashes()
#print(type(smorse(lst3[160542])))
#print(smorse("intransigence"))
#print(smorse(replacedN))
#perf_balan()
#palin_13()
only_13()





