def qcheck(array):
    array_set = set(array)
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    diag_check = 0
    coor_list = []
    diag_list1 = []
    diag_list2 = []
    diag_list3 = []
    diag_list4 = []
    
    if len(array_set) != len(array):
        print(False)

    else:
        while counter1 < len(array):
                coor_list.append([counter1+1, array[counter1]])
                counter1 += 1
        
        while counter2 < len(array):

            diag_list1.append([coor_list[counter3][0]+counter2, coor_list[counter3][1]+counter2])
            if diag_list1[counter2][0] == 8 or diag_list1[counter2][1] == 8:
                while counter4 < len(diag_list1):
                    if diag_list1[counter4] in coor_list:
                        diag_check += 1
                    counter4 += 1
                if diag_check > 1:
                    print(False)
                    break
                else:
                    counter3 += 1
                

            counter2 += 1
            
        print(diag_list1) 
                
        

#qcheck([4, 2, 7, 3, 6, 8, 5, 1])
#qcheck([2, 5, 7, 4, 1, 8, 6, 3])
#qcheck([5, 3, 1, 4, 2, 8, 6, 3])
qcheck([5, 8, 2, 4, 7, 1, 3, 6])
#qcheck([4, 3, 1, 8, 1, 3, 5, 2])




