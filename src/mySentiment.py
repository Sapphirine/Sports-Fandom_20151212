import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import json as simplejson
from copy import deepcopy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
f=open('tweets_for_nlp_analysis.txt', 'r')

#f=open('/Users/qiansheng/Desktop/big data/project/sentiment_code/testfile.txt', 'r')
of=open('output.txt', 'w')
scores={}
team_list=['Hawks', 'Celtics', 'Bulls', 'Cavaliers', 'Mavericks', 'Nuggets', 'Pistons', 'Warriors', 'Rockets', 'Pacers', 'Clippers', 'Lakers', 'Grizzlies', 'Heat', 'Bucks', 'Timberwolves', 'Nets', 'Hornets', 'Knicks', 'Thunder', 'Magic', 'Sixers', 'Suns', 'Blazers', 'Kings', 'Spurs', 'Raptors', 'Jazz', 'Wizards', 'Pelicans'
 ]
teamID_map={}

team_hash_codes = open('team_hash_codes.txt', "r")
team_hash = simplejson.load(team_hash_codes)
team_hash_codes.close()

# test_list=['1','3','4']
# for j in range(0,len(test_list)):
#     teamID_map[test_list[j]]=team_list[j]
for team in team_list:
    scores[team]=0

teamID_map = team_hash
#print teamID_map
team_map = {}
for key in teamID_map:
    team_map[str(key)] = str(teamID_map[key])
teamID_map = team_map
print teamID_map

team_dict = {v: k for k, v in teamID_map.items()}
print team_dict

score_dic={}
user_list=[]
team_mentioned={}
for line in f:
     paragraph = line
     components = paragraph.split(',', 2)
     #print components[0]
     #print components[1]
     #print components[2]
     if components[0] not in user_list:
         score_dic[components[0]]=deepcopy(scores)
         team_mentioned[components[0]]=deepcopy(scores)
         user_list.append(components[0])
     team_mentioned[components[0]][teamID_map[components[1]]]=1
     sid = SentimentIntensityAnalyzer()
     ss=sid.polarity_scores(components[2])
     if ss['compound']>=0:
         score_dic[components[0]][teamID_map[components[1]]]+=1
     else:
         score_dic[components[0]][teamID_map[components[1]]]-=1

f.close()
print score_dic
for user in score_dic:
     #print score_dic[user]
     #print team_mentioned[user]
     for team in score_dic[user]:
         score_tmp=0
         if team_mentioned[user][team]==1:
             if score_dic[user][team] == 0:
                 score_tmp=0.5
             else:
                 score_tmp=score_dic[user][team]
             of.write(user+','+team_dict[team]+','+str(score_tmp)+'\n')
of.close()
