# -*- coding: utf-8 -*-

# compute the times of action(rec|click|msg) for each user

from math import sqrt

def getActionScore(action):  
  if action == "rec": 
    return 0
  elif action == "click"  :    
    return 1 
  else:  
    return 2
	
def compute_interaction(data): 
  interaction = {}

  for line in data:   
    (userA,userB,times,action) = line.split(' ')  
    action = action[:-1]
    key = userB + " " + action
    interaction.setdefault(key, 0)
    interaction[key] += 1

  return interaction 

def compute_user_history_interaction(trainFile):
  records = []
  lineList = []
  lineNum = 1
  result = []
  
  lineList = [line for line in file(trainFile)]
  for line in lineList:
    if lineNum == 1:	#ignore the title in first line
      lineNum += 1
      continue

    records.append(line)
    lineNum += 1

  interaction = compute_interaction(records)  

  out = file('user_interaction.txt', 'w')
  for (key, times) in interaction.items(): 
    out.write('%s %d' % (key, times))
    out.write('\n')

  for (key, times) in interaction.items():
    user, action = key.split(' ');
    result.append((user, action, times))
  
  return result

#get the weight for each type of action
def get_action_weight(action):
  pop = 0;
  if action == "rec":
    pop = 1
  elif action == "click":
    pop = 10
  elif action == "msg":
    pop = 100

  return pop;

#trainFile line like: [userA, userB, action_times, action_type(rec|click|msg)]
def compute_user_popularity(trainFile, user_popularity_file):
  popDict = {}
  rankedscores = []
  result = []
  
  print "-----compute_user_history_interaction ... "
  
  interaction = compute_user_history_interaction(trainFile)
  
  print "-----compute_user_popularity ... "
  
  for (user, action, times) in interaction[0:len(interaction)]:
    popDict.setdefault(user, 0)
    popDict[user] += get_action_weight(action) * times

  ranked_popularity = [(popularity, user) for (user, popularity) in popDict.items()]
  ranked_popularity.sort()
  ranked_popularity.reverse()

  print "-----ranking_user_popularity ... "
  
  result = [(user, popularity) for (popularity, user) in ranked_popularity[0:len(ranked_popularity)]]

  print "-----output user_popularity ... "
  
  out = file(user_popularity_file, 'w')
  for (user, popularity) in result[0:len(result)]: 
    out.write('%s %d\n' % (user, popularity))

  print "-----Ending ... "

  return result