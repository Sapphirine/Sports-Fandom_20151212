import time
from twitter import *
from collections import defaultdict
import os

# REPLACE WITH YOUR INFO
consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

for fn in os.listdir('./team_users/'):
	i = open('./team_users/' + fn, "r")
	print "working with file: " + fn
	users = []
	for line in i:
		users.extend(line.split(", "))

	team_list_file = open("./team_files/team_list.txt", "r")

	team_list = []
	for line in team_list_file:
		team_list.extend(line.lower().split(", "))

	all_tweets = open('./tweets/' + fn + "_tweets.txt", "w")

	for x in range(0, 900, 300):
		currlist = users[x:x+300]
		for user_id in currlist:
			try:
				tweets = twitter.statuses.user_timeline(id=user_id)
			except:
				continue
			if tweets == []:
				continue

			all_tweets.write(user_id+"\n")
			all_tweets.write(str([tweet["text"] for tweet in tweets]) + "\n")

		print "waiting for next iteration"
	 	time.sleep(15*60)
	print "done with file: " + fn
	all_tweets.close()
	i.close()

