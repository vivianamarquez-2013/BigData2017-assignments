#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-user-search
#  - performs a search for users matching a certain query
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# perform a user search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/search
#-----------------------------------------------------------------------
results = twitter.users.search(q = '"Obama"')

#-----------------------------------------------------------------------
# loop through each of the users, and print their details
#-----------------------------------------------------------------------
for user in results:
	print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])
