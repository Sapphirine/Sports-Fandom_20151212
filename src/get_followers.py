from twitter import *
import time

# Enter credentials here
consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

team_list_file = open("team_twitter_handles.txt", "r")

team_list = []
for line in team_list_file:
	team_list.extend(line.lower().split(", "))

for team in team_list:
	ids_to_write = []
	results = twitter.followers.ids(screen_name=team, cursor=-1)
	count = 0
	while results != None and count < 12:
		ids_to_write.extend(results["ids"])
		count = count + 1
		results = twitter.followers.ids(screen_name=team, cursor=results["next_cursor"])
	ids_to_write.sort()
	team_file = open('team_users/' + team + "_users", "w")		
	for twitter_id in ids_to_write:
		team_file.write(str(twitter_id) + ", ")
	team_file.close()
	print "done with " + team
	time.sleep(15*60)