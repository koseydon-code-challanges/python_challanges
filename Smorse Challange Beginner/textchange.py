fileinput = open("/Users/denizhasirci/Desktop/Python Works/Smorse Challange Beginner/enable1.txt", "r")

inputread = fileinput.read()

inputread.replace('\n', '')

print(inputread)