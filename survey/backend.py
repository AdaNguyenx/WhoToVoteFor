import urllib2
import operator
import json
import pprint

def findLegislators1(userstate):

	url = urllib2.Request("https://api.fiscalnote.com/legislators?apikey=49BWNS84OZ0Y9CYZW4EJ7A7PVBFCY46N")

	response = urllib2.urlopen(url)

	response = response.read()

	legislators = json.loads(response)
	list_of_legistrators = []
	state = userstate

	for rep in legislators:
		if (rep['state'] == userstate and rep['party'] == "Democratic"):
			list_of_legistrators.append(rep)
	return list_of_legistrators

def findLegislators2(userstate):

	url = urllib2.Request("https://api.fiscalnote.com/legislators?apikey=49BWNS84OZ0Y9CYZW4EJ7A7PVBFCY46N")

	response = urllib2.urlopen(url)

	response = response.read()

	legislators = json.loads(response)
	list_of_legistrators = []
	state = userstate

	for rep in legislators:
		if (rep['state'] == userstate and rep['party'] == "Republican"):
			list_of_legistrators.append(rep)
	return list_of_legistrators