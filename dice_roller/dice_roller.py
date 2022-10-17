from random import randint

def dice_roller():
    dice_list = input("Please enter your dice: ").split("d")
    roll_number, dice_size = int(dice_list[0]), int(dice_list[1])
    c = 0
    list1 = []
    while c < roll_number:
        list1.append(randint(1,dice_size))
        c += 1
    result = str(sum(list1))
    roll_list = ""
    for rolls in list1:
        roll_list += " " + str(rolls)
   
    print("{} :{}".format(result, roll_list))


dice_roller()

