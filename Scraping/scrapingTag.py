import sys, os
from urllib import urlopen
from lxml import html
import requests
import json
from requests.exceptions import ChunkedEncodingError
import dbTag
import sys

def trim_string(string):
	string = string.replace('"','')
	string = string.replace("'","")
	return string

def get_TS_tag(channel_id):
	url = 'https://thingspeak.com/channels/{}'.format(channel_id)
	page = requests.get(url)
	tree = html.fromstring(page.content)
	tags = tree.xpath('//*[@id="channel-tags"]/text()')

	return tags

def get_SF_tag(channel_id):
	url = 'https://data.sparkfun.com/streams/' + channel_id + '.json'
	tags = []
	
	try:
		response = requests.get(url)
		data_channel = json.loads(response.content)
		channel_doc = data_channel['stream']['_doc'] 
		channel_id = trim_string(data_channel['publicKey']).decode('utf-8')
		tags = channel_doc['tags']
	except:
		print(sys.exc_info()[0])
		pass
		
	return tags

def scrape_and_store_tag(channel_id,provenance):
	tags = []

	if (provenance == "ThingSpeak"):
		tags = get_TS_tag(channel_id)
	elif(provenance == "SparkFun"):
		tags = get_SF_tag(channel_id)
			
	database = db.MyDB()

	for tag in tags:
		database.insert_tag(tag,channel_id)		

if __name__ == "__main__":

	database = dbTag.MyDB()

	TS_channels = database.get_all_channels_id('ThingSpeak')
	SF_channels = database.get_all_channels_id("SparkFun")
	
	'''
	for channel in TS_channels:
		scrape_and_store_tag(channel[0],"ThingSpeak")
	'''

	for channel in SF_channels:
		scrape_and_store_tag(channel[0],"SparkFun")
	
