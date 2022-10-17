def hexcolor(red, green, blue):
    print("#{}{}{}".format(hex(red)[2:].upper(),hex(green)[2:].upper(),hex(blue)[2:].upper()))

hexcolor(255, 99, 71)
hexcolor(115, 100, 64)
hexcolor(189, 183, 107)


def blend(color_list):
    counter = red = green = blue = 0

    while counter < len(color_list):

        red += int(color_list[counter][1:3], 16)
        green += int(color_list[counter][3:5], 16)
        blue += int(color_list[counter][5:7], 16)
        counter += 1
        
    total_red = int(red/counter)
    total_green = int(green/counter)
    total_blue = int(blue/counter)


    hexcolor(total_red, total_green, total_blue)

blend(["#E6E6FA", "#FF69B4", "#B0C4DE", "#FF6347"])
