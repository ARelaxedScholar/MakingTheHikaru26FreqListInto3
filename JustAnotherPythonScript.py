#Change and remix this as you see fit, the utf-8 is necessary to allow python to deal with japanese text, so don't remove that.
#For the rest you can change it as you see fit.
# -*- coding: utf-8 -*-
file = open("actual_hikaru_list.txt", "r", encoding="utf-8") # <= just edit here if you want to change the source file
#           ||
#Edit these \/ if you want to change the output file names to something relevant to you
output1 = open("hikaruFreqListWithoutFreqCore10K.txt", "w", encoding="utf-8") 
output2 = open("hikaruFreqListWithoutFreqCore10k-20k.txt", "w", encoding="utf-8")
output3 = open("hikaruFreqListWithoutFreqCore20k-26k.txt", "w", encoding="utf-8")

tempList = []
newList = []
for line in file:
    tempList.append(line.split())

#Finally edit the ranges here to change how many lines are put in a given file, range(0,10000) will go from 0th line to 9999th line.
for i in range(0,10000):
    output1.write(tempList[i][0]+"\n")
for i in range(10000,20000):
    output2.write(tempList[i][0]+"\n")
for i in range(20000,len(tempList)):
    output3.write(tempList[i][0]+"\n")

file.close()
output1.close()
output2.close()
output3.close()

print("Complete")

    
    
