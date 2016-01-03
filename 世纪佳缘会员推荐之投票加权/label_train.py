# -*- coding: utf-8 -*-

from math import *

def labelstrain_v1(data):
  labels = []
  lst_userA = "="
  userBActionList = ""
  
  for line in data:
    (userA, userB, round, action) = line.split(' ')
    action = action[:-1]

    if userA == "USER_ID_A":
      continue

    if lst_userA == "=":
      userBActionList += getActionScore_v1(action)
    elif userA == lst_userA:
      userBActionList += " " + getActionScore_v1(action)
    else:
      labels.append(userBActionList)
      userBActionList = ""
      userBActionList += getActionScore_v1(action)
    lst_userA = userA

  labels.append(userBActionList)	#for the last group

  return labels

def getActionScore_v1(action):  
  if action == "rec": 
    return "0"
  elif action == "click":
    return "1"
  elif action == "msg":
    return "2"

def labels_train_v1(train_sort_File):
  records = [line for line in file(train_sort_File)]

  print len(records)
  labels = labelstrain_v1(records)
  print len(labels)

  out = file('labels_train_v1.txt', 'w')
  for (userBList) in labels[0:len(labels)]: 
    out.write('%s\n' % (userBList))


def labelstrain_v2(data):
  labels = []
  lst_userA = "="
  userBAction = {}
  userBActionList = ""
  Records = []
  userRecRecords = ""
  
  for line in data:
    (userA, userB, round, action) = line.split(' ')
    action = action[:-1]

    if userA == "USER_ID_A":
      continue

    if lst_userA == "=" or userA == lst_userA:
      key = (int(userA), int(userB))
      userBAction.setdefault(key, -1)
      userBAction[key] = max(userBAction[key], getActionScore_v2(action))
    else:
      line = 1
      keys = userBAction.keys()
      keys.sort()	#dict may be no order, should sort by key
      for key in keys:
        if line == 1:
          userBActionList += str(userBAction[key])
          userRecRecords += str(key[0]) + " " + str(key[1])
        else:
          userBActionList += " " + str(userBAction[key])
          userRecRecords += " " + str(key[1])
        line += 1
      labels.append(userBActionList)
      Records.append(userRecRecords)

      userBAction = {}
      userBActionList = ""
      userRecRecords = ""
      key = (int(userA), int(userB))
      userBAction.setdefault(key, -1)
      userBAction[key] = max(userBAction[key], getActionScore_v2(action))
    lst_userA = userA

  #for the last group
  line = 1
  keys = userBAction.keys()
  keys.sort()	#dict may be no order, should sort by key
  for key in keys:
    if line == 1:
      userBActionList += str(userBAction[key])
      userRecRecords += str(key[0]) + " " + str(key[1])
    else:
      userBActionList += " " + str(userBAction[key])
      userRecRecords += " " + str(key[1])
    line += 1
  labels.append(userBActionList)
  Records.append(userRecRecords)

  return labels, Records

def getActionScore_v2(action):  
  if action == "rec": 
    return 0
  elif action == "click":
    return 1
  elif action == "msg":
    return 2

def labels_train_v2(train_sort_File, label_train_file, user_recommend_file):
  print "-----reading train file ... "
  
  records = [line for line in file(train_sort_File)]

  print "-----label train file ... "
  
  print len(records)
  labels, rec_records = labelstrain_v2(records)
  print len(labels)

  print "-----output label_train file ... "
  
  out = file(label_train_file, 'w')
  for (userBList) in labels[0:len(labels)]: 
    out.write('%s\n' % (userBList))

  print "-----output user recommend file ... "

  out = file(user_recommend_file, 'w')
  for (userA_BList) in rec_records[0:len(rec_records)]: 
    out.write('%s\n' % (userA_BList))

  print "Ending"

  
  
