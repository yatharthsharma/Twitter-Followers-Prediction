from twython import Twython, TwythonError
import csv
import time

consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_token_secret = 'XXX'


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)




try:
    with open('E:/Twitter_file/twitterData.csv', "rb") as csvfile:
        datareader = csv.reader(csvfile)
        for data in datareader:
            count = 0
            count_all = 0
            
            if int(data[7]) < 50000:
                iterate = (int(data[7])/200) + 1
                try:          
                    for i in range(iterate):
                        timeline = twitter.get_user_timeline(screen_name=str(data[2]),count=200,page = i+1)
                        
                        for tweet in timeline:
                            if len(tweet['text']) > 2:
                                if tweet['text'][0] != 'R':
                                    if tweet['text'][1] != 'T':
                                        count = tweet['retweet_count'] + count
                                count_all = tweet['retweet_count'] + count_all
                            else:
                                 count = tweet['retweet_count'] + count
                                 count_all = tweet['retweet_count'] + count_all
                    saveFile = open ('E:/Twitter_file/twitterData_retweet.csv','a')
                    saveFile.write(str(data[0]) + ',' +str(data[1]) + ',' + str(data[2]) + ',' + str(data[3]) + ',' + str(data[4]) + ',' + str(data[5]) + ',' + str(data[6]) + ',' + str(data[7]) + ',' + str(data[8])+ ',' + str(count_all)+ ',' + str(count))
                    saveFile.write('\n')
                    saveFile.close()           
                    #data_save = [str(data[0]) , str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(count_all),str(count)]
                except TwythonError as e:
                    print e
                    time.sleep(310)
    
                

            
except TwythonError as e:
    print e
    #time.sleep(310)
    








