def funnel(word1, word2):
    c = 1
    while c <= len(word1):
        new_str = word1[0:(c-1)] + word1[c:len(word1)]
        if new_str == word2:
            print(True)
            break
        else:
            c += 1
    else:
        print(False)

funnel("leave", "eave") 
funnel("reset", "rest")
funnel("dragoon", "dragon") 
funnel("eave", "leave") 
funnel("sleet", "lets") 
funnel("skiff", "ski")

inputread = open("/Users/denizhasirci/Desktop/Python Works/Challanges/Smorse Challange Beginner/enable1.txt", "r").read()
replacedN = inputread.replace("\n", " ")
word_lst = replacedN.split(" ")

def bonus(word1):
    out_lst = []
    c = 1
    while c <= len(word1):
        new_str = word1[0:(c-1)] + word1[c:len(word1)]
        if new_str in word_lst and new_str not in out_lst:
            out_lst.append(new_str)
        c += 1
    return out_lst
    #print(out_lst)


bonus("dragoon")
bonus("boats")
bonus("affidavit")

def bonus2():
    five_list = []
    c = 0
    for every in word_lst:
        print(c)
        if len(bonus(every)) == 5:
            five_list.append(every)
        word_lst.pop(c)
        c += 1        
    print(five_list)

bonus2()

        

    
