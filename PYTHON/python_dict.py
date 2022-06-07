from tkinter.tix import DirTree


dict1 = {}

dict1[1] = []

dict1[1].append(2)
dict1[1].append(5)

print(dict1)

print (dict1[1][0])

if 2 in dict1:
    print("you")
else:
    print ('wu')