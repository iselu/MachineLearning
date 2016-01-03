# -*- coding: utf-8 -*-


import time, datetime
from math import *

def extract_feature_status(records_m, records_f):
  #features: last_login_time, finding_friend, login_count, has_picture
  feature_status = []
  feature = ""

  for line in records_m:
    feature = ""
    fields = line.split('\t')
    user_id = fields[0]
    last_login_time = fields[3]
    finding_friend = fields[8]
    login_count = fields[9]
    has_picture = fields[22]
    feature = user_id + " " + last_login_time + " " + finding_friend + " " + login_count + " " + has_picture
    feature_status.append(feature)

  for line in records_f:
    feature = ""
    fields = line.split('\t')
    user_id = fields[0]
    last_login_time = fields[3]
    finding_friend = fields[8]
    login_count = fields[9]
    has_picture = fields[22]
    feature = user_id + " " + last_login_time + " " + finding_friend + " " + login_count + " " + has_picture
    feature_status.append(feature)

  out = file('user_feature_status.txt', 'w')
  for feature in feature_status[0:len(feature_status)]:
    out.write('%s' % (feature))
    out.write('\n')

  return feature_status 

def compute_feature_vector(feature_status, popDic):
  #features vector: user_popularity, user_active, user_demand, user_count, user_sincerity
  feature_vector = {}
  counts = {}
  benchmark_time = int(time.mktime(datetime.datetime(2011, 1, 1).timetuple()))
  
  for line in feature_status:
    user_id, last_login_time, finding_friend, login_count, has_picture = line.split(' ')

    if user_id not in popDic:
      continue

    if user_id in popDic:    #featrue 1
      popularity = popDic[user_id]
    else:
      popularity = 0
    if int(last_login_time) >= benchmark_time:    #featrue 2
      active = 1
    else:
      active = 0
    if int(finding_friend) == 1:    #featrue 3
      demand = 1
    else:
      demand = 0
    if int(last_login_time) >= benchmark_time:    #featrue 4
      count = int(login_count)
    else:
      count = 0
    counts[user_id] = count
    if int(has_picture) == 1:    #featrue 5
      sincerity = 0.8
    else:
      sincerity = 0.2

    vector = (popularity, active, demand, count, sincerity)
    feature_vector[user_id] = vector
  
  #normalize
  vsmall = 1 # Avoid division by zero errors
  max_count = max(counts.values())
  if max_count == 0: max_count = vsmall
  for (user_id, count) in counts.items():
    vector1 = feature_vector[user_id]
    vector2 = (vector1[0], vector1[1], vector1[2], float(count)/max_count, vector1[4])
    feature_vector[user_id] = vector2
  
  vsmall = 1 # Avoid division by zero errors
  max_popularity = max(popDic.values())
  if max_popularity == 0: max_popularity = vsmall
  for (user_id, popularity) in popDic.items():
    vector1 = feature_vector[user_id]
    vector2 = (float(popularity)/max_popularity, vector1[1], vector1[2], vector1[3], vector1[4])
    feature_vector[user_id] = vector2
  
  return feature_vector

def compute_user_score(profile_m, profile_f, user_popularity_file):
  records_m = []
  records_f = []
  popDic = {}
  user_score = {}
  
  print "-----reading male profile ... "
  
  records_m = [line for line in file(profile_m)]

  print "-----reading female profile ... "

  records_f = [line for line in file(profile_f)]

  print "-----reading user popularity file ... "
  
  for line in file(user_popularity_file):
    (user, popularity) = line.split(' ')
    popDic[user] = int(popularity[:-1])
  
  print "-----extract feature status ... "

  feature_status = extract_feature_status(records_m, records_f)
  
  print "-----compute feature vector ... "
  
  feature_vector = compute_feature_vector(feature_status, popDic)
  
  print "-----compute user score ... "
  
  for user_id, vector in feature_vector.items():
    (popularity, active, demand, count, sincerity) = vector
    score = 0.85 * popularity + 0.05 * (active + demand) + 0.03 * count + 0.02 * sincerity
    user_score[user_id] = score

  ranked_score = [(score, user) for (user, score) in user_score.items()]
  ranked_score.sort()
  ranked_score.reverse()
  
  result = [(user, score) for (score, user) in ranked_score[0:len(ranked_score)]]
  
  out = file('user_score.txt', 'w')
  for (user, score) in result[0:len(result)]: 
    out.write('%s %f' % (user, score))
    out.write('\n')
  
  return user_score