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

relevant_tweets = open('./tweets/relevant_tweets.txt', "w")
for fn in os.listdir('./tweets'):
	print "working with " + fn
	if fn == ".DS_Store" or fn == ".DS_Store_tweets.txt" or fn == "relevant_tweets.txt":
		continue
	i = open('./tweets/' + fn, "r")
	team_list_file = open("./team_files/team_list.txt", "r")
	team_list = []
	for line in team_list_file:
		team_list.extend(line.lower().split(", "))

	total_lines = os.stat('./tweets/' + fn).st_size
	total_count = 0
	for x in range(0, total_lines, 2):
		user = i.readline()
		tweets = i.readline()
		tweet_list = []
		tweet_string = ""
		prev_char = ''
		ready = False
		for char in tweets:
			if (char == "\"" or char == "\'") and prev_char == 'u':
				ready = True
			if ready:
				tweet_string+=char
			if (char == "," or char == ']') and (prev_char == "\"" or prev_char == "\'"):
				ready = False
				tweet_list.append(tweet_string)
				tweet_string = ""
			prev_char = char
		true_tweets = []
		true_tweets.append(fn)
		true_tweets.append(user.strip())
		of_relevance = False
		for tweet in tweet_list:
			words = tweet.split()
			words = [word.lower() for word in words]	
			for team in team_list:
				if team in words:
					true_tweets.append(tweet)
					of_relevance = True
		if of_relevance:
			simplejson.dump(true_tweets, relevant_tweets)
			relevant_tweets.write("\n")
	i.close()
relevant_tweets.close()

