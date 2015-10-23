import json
from datetime import datetime
tweets_data_path = 'C:/Python27/twitter.txt'


tweets_data = []
tweets_file = open(tweets_data_path,'r')
count = 0
for line in tweets_file:
    try:
        
         tweet = json.loads(line)
         tweets_data.append(tweet)
         count = count + 1
         data = [tweet['user']['id'] , tweet['user']['name'] , tweet['user']['screen_name'] , tweet['user']['followers_count'] , tweet['user']['friends_count'] , tweet['user']['listed_count'] , tweet['user']['favourites_count'] ,  tweet['user']['statuses_count'] , tweet['user']['created_at']]
         date_object = datetime.strptime(data[8], "%a %b %d %H:%M:%S +0000 %Y")
         diff =  datetime.now()- date_object
         saveFile = open ('twitterDataF.csv','a')
         saveFile.write(str(data[0]) + ',' +str(data[1]) + ',' + str(data[2]) + ',' + str(data[3]) + ',' + str(data[4]) + ',' + str(data[5]) + ',' + str(data[6]) + ',' + str(data[7]) + ',' + str(diff.days))
         saveFile.write('\n')
         saveFile.close()
         
        
        
    except:
        
        continue
    
print count

