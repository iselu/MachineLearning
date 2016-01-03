# -*- coding: utf-8 -*-

from math import sqrt
from operator import itemgetter

def compute_ranks_using_popularity(user_recommend_file, user_popularity_file, rank_file):
  all_user_list = []
  
  user_rec_rank = ""
  all_user_rec_rank = []
  
  userB_popularity = {}
  all_user_popularity = {}
  
  userB_ranking = {}
  
  print "reading user popularity ... "
  
  for line in file(user_popularity_file):
    line = line[:-1]
    user, popularity = line.split(' ')
    all_user_popularity[user] = int(popularity)
  
  print "calculating user recommend ranking ... "
  
  for line in file(user_recommend_file):
    user_rec_rank = ""
    userB_popularity = {}
    userB_ranking = {}

    line = line[:-1]
    all_user_list = line.split(' ')
    userA = all_user_list[0]
    userB_list = all_user_list[1:len(all_user_list)]
    for userB in userB_list:
      if userB in all_user_popularity:
        userB_popularity[userB] = all_user_popularity[userB]
      else:
        userB_popularity[userB] = 0

    ranked_userB_popularity = [(popularity, userB) for (userB, popularity) in userB_popularity.items()]
    ranked_userB_popularity.sort()
    ranked_userB_popularity.reverse()

    ranking = 1
    for (popularity, userB) in ranked_userB_popularity[0:len(ranked_userB_popularity)]:
      userB_ranking[userB] = ranking
      ranking += 1

    line = 1
    for userB in userB_list:
      if line == 1:
        user_rec_rank += str(userB_ranking[userB])
      else:
        user_rec_rank += " " + str(userB_ranking[userB])
      line += 1

    all_user_rec_rank.append(user_rec_rank)

  print "output ranking file ... "
  
  out = file(rank_file, 'w')
  for user_rec_rank in all_user_rec_rank[0:len(all_user_rec_rank)]: 
    out.write('%s\n' % (user_rec_rank))

  print "Ending"
  
def compute_ranks_using_score(user_recommend_file, user_score_file, rank_file):
  all_user_list = []
  
  user_rec_rank = ""
  all_user_rec_rank = []
  
  userB_score = {}
  all_user_score = {}
  
  userB_ranking = {}
  
  print "reading user score ... "
  
  for line in file(user_score_file):
    line = line[:-1]
    user, score = line.split(' ')
    all_user_score[user] = float(score)
  
  print "calculating user recommend ranking ... "
  
  for line in file(user_recommend_file):
    user_rec_rank = ""
    userB_score = {}
    userB_ranking = {}

    line = line[:-1]
    all_user_list = line.split(' ')
    userA = all_user_list[0]
    userB_list = all_user_list[1:len(all_user_list)]
    for userB in userB_list:
      if userB in all_user_score:
        userB_score[userB] = all_user_score[userB]
      else:
        userB_score[userB] = 0

    ranked_userB_score = [(score, userB) for (userB, score) in userB_score.items()]
    ranked_userB_score.sort()
    ranked_userB_score.reverse()

    ranking = 1
    for (score, userB) in ranked_userB_score[0:len(ranked_userB_score)]:
      userB_ranking[userB] = ranking
      ranking += 1

    line = 1
    for userB in userB_list:
      if line == 1:
        user_rec_rank += str(userB_ranking[userB])
      else:
        user_rec_rank += " " + str(userB_ranking[userB])
      line += 1

    all_user_rec_rank.append(user_rec_rank)

  print "output ranking file ... "
  
  out = file(rank_file, 'w')
  for user_rec_rank in all_user_rec_rank[0:len(all_user_rec_rank)]: 
    out.write('%s\n' % (user_rec_rank))

  print "Ending"