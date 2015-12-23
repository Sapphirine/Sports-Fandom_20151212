import time
from twitter import *
from collections import defaultdict
import os
import json as simplejson

# REPLACE WITH YOUR NAME

team_dicts = {"Hawks": ["Hawks","@ATLHawks"], "Celtics": ["Celtics","@celtics"],"Bulls": ["Bulls","@chicagobulls"],"Cavaliers": ["Cavaliers","@cavs"],"Mavericks": ["Mavericks","@dallasmavs"],"Nuggets": ["Nuggets","@nuggets"],"Pistons": ["Pistons","@DetroitPistons"],"Warriors": ["Warriors","@warriors"],"Rockets": ["Rockets","@HoustonRockets"],"Pacers": ["Pacers","@Pacers"],"Clippers": ["Clippers","@LAClippers"],"Lakers": ["Lakers","@Lakers"],"Grizzlies": ["Grizzlies","@memgrizz"],"Heat": ["Heat","@MiamiHEAT"],"Bucks": ["Bucks","@Bucks"],"Timberwolves": ["Timberwolves","@Timberwolves"],"Nets": ["Nets","@BrooklynNets"],"Hornets": ["Hornets","@hornets"],"Knicks": ["Knicks","@nyknicks"],"Magic": ["Magic","@OrlandoMagic"],"Sixers": ["Sixers","@Sixers"],"Suns": ["Suns","@Suns"],"Blazers": ["Blazers","@trailblazers"],"Kings": ["Kings","@SacramentoKings"],"Spurs": ["Spurs","@spurs"],"Raptors": ["Raptors","@Raptors"],"Jazz": ["Jazz","@utahjazz"],"Wizards": ["Wizards","@WashWizards"],"Thunder": ["Thunder","@okcthunder"], "Pelicans": ["Pelicans","@PelicansNBA"]}
team_dict = {value:key for key in team_dicts for value in team_dicts[key]}
newDict = eval(repr(team_dict).lower())
team_dict = newDict

team_list_file = open("./team_files/team_list.txt", "r")
team_list = []
for line in team_list_file:
	team_list.extend(line.lower().split(", "))

mahout_out = open("mahout_input_no_sentiment", "w")

relevant_tweets = open('./tweets/relevant_tweets.txt', "r")
team_name = ""
for line in relevant_tweets:
	user_tweets = simplejson.loads(line)
	team_name = user_tweets[0]
	user_id = user_tweets[1]
	user_dict = {}
	for tweet in user_tweets[2:]:
		words = tweet.split()
		for word in words:
			word = word.lower()
			if word in team_list:
				user_dict[team_dict[word]] = user_dict.get(team_dict[word]	, 0) + 1

	for key in user_dict:
		mahout_out.write(str(user_id)+ "," + str(abs(hash(key.lower())/100000000000)) + "," + str(user_dict[key]) + "\n")
relevant_tweets.close()

