# big-data-analytics

Sports Fandom

Columbia Big Data Analytics

Fall 2015

Brian Slakter, Mayank Mahajan, Sheng Qian

Pulling Data

Pulling Users

The following python script must be modified to contain your Twitter API credentials where indicated by comments in the script. The script will pull ~1000 user IDs who follow each NBA team twitter account, and save the users for each team to a file.

python get_followers.py

Pulling Tweets

The following python script must be modified to contain your Twitter API credentials where indicated by comments in the script. This will pull tweets from the users identified from the previous script and save their tweets.

python pull_tweets_and_save.py

Identifying Relevant Tweets

The script below will parse through the tweets saved and identify those tweets that mention other NBA teams, and save them to a separate file.
python extract_relevant_tweets.py

Mahout

Generating Mahout Input

No Sentiment Analysis

The python script below counts each mention of a team as a positive mention, and generates a file containing user-team pairs and the number of mentions for that pair.

python generate_counts_without_sentiment.py

Sentiment Analysis

To perform sentiment analysis, we first run a script to adjust the format of the data such that there is one tweet per line. python generate_file_for_sentiment_analysis.py

To then perform the sentiment analysis, we run a script that reads through this created file and generates a score for each user-team combination and outputs the results to a file. python mySentiment.py

Mahout Analysis

The Java program referenced below generates recommendations for the input that has been analyzed ia NLP as well as the input that has not. The program will generate outputs listing user-team recommendation pairs, with the associated score representing the strength of the recommendation.
Rec.java

System G

Generating SystemG Input:

The script below generates a file of nodes (users and teams), and lists a description so that filtering can be performed within SystemG

python build_nodes_for_system_g.py

The input to Mahout (analyzed for sentiment) can be used as the input "edges" file.

SystemG Visualizations:

Simply upload the "nodes" and "edges" files mentioned above into the system and generate the graph.
