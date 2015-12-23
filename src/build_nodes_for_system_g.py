import time
from twitter import *
from collections import defaultdict
import os
import json as simplejson

# REPLACE WITH YOUR NAME
relevant_tweets = open('./tweets/relevant_tweets.txt', "r")
nodes_out = open("nodes",'w')
team_hash_codes = open('./team_files/team_hash_codes.txt', "r")
team_dict = simplejson.load(team_hash_codes)
team_hash_codes.close()
nodes_out.write("id,group\n")
for line in relevant_tweets:
	user_tweets = simplejson.loads(line)
	team_file_name = user_tweets[0]
	team_name_array = team_file_name.split('_')
	team_name = team_name_array[0]
	user_id = user_tweets[1]
	nodes_out.write(user_id+","+team_name+"\n")
for key in team_dict:
	nodes_out.write(str(int(key))+",TEAM-"+team_dict[key]+"\n")
nodes_out.close()	
relevant_tweets.close()