import random
import tweepy

# This is setting up our authentication so Twitter knows who we are!
TWITTER_CONSUMER_KEY = 'E4c30HUmpB8O0fsjA0IVcsP8F'
TWITTER_CONSUMER_SECRET = 'FBIFejFzogxSdCDBdDriYFpOOoLvYrOPuVSdIvyg286i0VhiRL'
TWITTER_ACCESS_KEY = '910235671108784129-2fpwQz8UVZkY2aEz3PzLmaaWUhNwQh1'
TWITTER_ACCESS_SECRET = 'vcpWHzqJtWHiLlrm7NLN69EwugEf2knAUu4Kf7ulTEC7n'

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)

# Then we initialize our instance of Twitter
twitter = tweepy.API(auth)

# Now we can send tweets!
twitter.update_status("Hello World!")

file = open("quotes.txt", "r")
i = file.read(1)
newstring = ""
numlines = 0
x = random.randint(1, 3099)
z = 0
print(numlines)
print(x)
#line = file[0]
for line in file:
	z+=1
	if z == x:
		for i in range(len(line)):
			while line[i] != "%":
				newstring+=line[i]
			if len(newstring) == 0:
				print("equals 0")

