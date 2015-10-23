from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'XXX'
csecret = 'XXX'
atoken = 'XXX'
asecret = 'XXX'

class listener(StreamListener):

    def on_data(self, data):
        try :
            print data
            saveFile = open ('twitter.txt','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed'
            time.sleep(1)

    def on_error(self, status):
        print status
track = ['car' , 'modi' , 'obama' , 'india' , 'USA' ,'arsenal' ,'football']
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=track)



