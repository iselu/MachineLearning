# -*- coding: utf-8 -*-


#对数据集进行排序

def train_sort(trainFile, sortFile):
  records = []
  rankedLine = []
  lineNum = 1
  
  lineList = [line for line in file(trainFile)]
  for line in lineList:
    if lineNum == 1:	#ignore the title in first line
      lineNum += 1
      continue

    records.append(line)
    lineNum += 1
  
  for line in records:   
      list = line.strip('\n').split()  
#      print(list[3])
      rankedLine.append((int(list[0]), int(list[1]), list[2], list[3]))

  rankedLine.sort()
  #rankedLine.reverse()
  
  out = file(sortFile, 'w')
  for (userA_ID, userB_ID, times, action) in rankedLine[0:len(rankedLine)]: 
    out.write('%d %d %s %s\n' % (userA_ID, userB_ID, times, action))
  
  return rankedLine

train_sort('F:\\1.txt','F:\\2.txt')

print("-------------code completed--------------")




