# __author__ = 'litongyang'



# str2 = []
# for line in open("C:\\Users\\\Thinkpad\\Desktop\\data2.txt"):
#     linone = line.split('.')
#     try:
#         str2.append(linone[1])
#     except:
#         str2.append(linone[0])
#         pass
# fl = open("C:\\Users\\\Thinkpad\\Desktop\\res1.txt", 'w')
# for i in range(0, len(str2)):
#     fl.write(str2[i])

str1 = []
for line in open("C:\\Users\\\Thinkpad\\Desktop\\res1.txt"):
    linone = line.split()
    addStr = "T7" + "."
    try:
        linone[0] = addStr + linone[0]
        str1.append(linone[0])
    except:
        pass
fl = open("C:\\Users\\\Thinkpad\\Desktop\\res.txt", 'w')
for i in range(0, len(str1)):
    fl.write(str1[i])
    fl.write("\n")
