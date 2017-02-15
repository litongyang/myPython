# __author__ = 'lty'
# -*- coding: utf-8 -*-

f1 = open("/Users/litongyang/Desktop/11.txt", 'r')
f2 = open("/Users/litongyang/Desktop/22.txt", 'r')
f3 = open("/Users/litongyang/Desktop/33.txt", 'wr')
x_1 = []
y_1 = []
x_2 = []
y_2 = []
for line in f1:
    line_one = line.split('\t')
    x_1.append(str(line_one[0]).replace(' ', '').replace('\n', ''))
    y_1.append(str(line_one[2]).replace(' ', '').replace('\n', ''))
print x_1
print y_1
for line in f2:
    line_one = line.split('\t')
    x_2.append(str(line_one[0]).replace(' ', '').replace('\n', ''))
    y_2.append(str(line_one[1]).replace(' ', '').replace('\n', ''))
print x_2
print y_2
tmp = [val for val in x_1 if val in x_2]
print len(tmp)
for i in range(0, len(x_2)):
    if x_2[i] in tmp:
        for j in range(0, len(x_1)):
            if x_2[i] == x_1[j]:
                f3.write(str(x_2[i]))
                f3.write('\t')
                f3.write(str(y_2[i]))
                f3.write('\t')
                f3.write(str(y_1[j]))
                f3.write('\n')
    else:
        f3.write(str(x_2[i]))
        f3.write('\t')
        f3.write(str(y_2[i]))
        f3.write('\t')
        f3.write('')
        f3.write('\n')
# while i < len(x_2):
#     for j in range(0, len(x_1)):
#         if x_2[i] == x_1[j]:
#             f3.write(str(x_2[i]))
#             f3.write('\t')
#             f3.write(str(y_2[i]))
#             f3.write('\t')
#             f3.write(str(y_1[j]))
#             f3.write('\n')
#             i += 1
#             break
#         else:
#             f3.write(str(x_2[i]))
#             f3.write('\t')
#             f3.write(str(y_2[i]))
#             f3.write('\t')
#             f3.write('')
#             f3.write('\n')
#             i += 1
#             break

