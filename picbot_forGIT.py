import glob
import random
from PIL import Image
import tweepy
import time
from datetime import datetime

#print(glob.glob("/Users/masonbenge/Desktop/tweepy/pics/*"))

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

global blacklist
global number

blacklist = set()

def meme():
    
    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    
    for i in range (0,1):
        
        filename = random.choice(glob.glob("your file path to meme folder here followed by this star --->/*"))

        
        api.update_with_media(filename, 'Nice')
        
        api.update_status(f"The last tweet was made in {number} seconds and pushed out at {current_time}. When do you think the next one will go? ")

def countdown(n):
    
    while n>0:
        print(n)
        time.sleep(1)
        n = n-1
        if n == 0:
            meme()
    

number = random.choice(range(1,10000))

while True:
    countdown(5)
