#!/usr/bin/env python
# -*- coding: utf-8 -*-

# With this script we save all the data coming from SparkFun.

import sys, os
from urllib import urlopen
import requests
import json
from requests.exceptions import ChunkedEncodingError
import dbScraping


# We save all the stream IDs in a macro list, ready to be processed
# maxPages : number of pages to fetch in total
# threshold : number of pages after which start to parse along
def get_all_streams(maxPages, threshold):
	pageArray = [] # List of HTML pages (a pool)
	list_stream = [] # List of stream IDs
	
	# Start from the streams you already collected
	#list_stream += get_all_streams_local()

	# Fetch all the pages in the desired range
	# We get first HTML code and, once in a while, we parse them, empty the pool, and save the stream IDs
	counter = 0
	for i in range(0, maxPages):
		try:
			print "Getting page " + str(i) + "..."
			pageArray.append(urlopen("https://data.sparkfun.com/streams/?page=" + str(i)))
			
			# Start to parse from the pool (along one by one)
			if (i >= threshold) or (i >= maxPages - 1):
				html = pageArray.pop()
				list_stream += get_streams_from_html(html, list_stream)
		except:
			print (sys.exc_info()[0])
			continue
	# Empty the pool and parse the remainder
	for y in range(len(pageArray)):
		html = pageArray.pop()
		list_stream += get_streams_from_html(html, list_stream)
	print ("All in all we have " + str(len(list_stream)) + " streams to compute.")
	return list_stream

			
# Returns a list of stream URLs got from the HTML page
def get_streams_from_html(html, list_stream):
	list_stream_return = []
	for l in html.readlines():
		line = l.decode('utf-8').strip()  # All the lines tof the HTML document

		if "stream-title" in line:
			# Take the stream ID
			stream = line.split("\"")[3]
			if stream not in list_stream:
				list_stream_return.append(stream)

	return list_stream_return


def trim_string(string):
	string = string.replace('"','')
	string = string.replace("'","")
	return string

def get_stream_info(channels):
	list_valid_channels = []
	list_fields = []

	for channel in channels:
		print "Evaluating channel " + channel
		try:
			url = 'https://data.sparkfun.com' + channel + '.json'
			response = requests.get(url)
			data_channel = json.loads(response.content)

			channel_doc = data_channel['stream']['_doc'] 
			
			
			channel_id = trim_string(data_channel['publicKey']).decode('utf-8')

			
			database = dbScraping.MyDB()
			response = database.get_update(channel_id)
			del database
			if response == 0:
			
				channel_name = trim_string(channel_doc['title']).decode('utf-8')
				channel_description = trim_string(channel_doc['description']).decode('utf-8')

				dict = {'channel_id': channel_id,'name':channel_name,'description':channel_description}
				
				list_valid_channels.append(dict)
				
				count = 0
				fields = channel_doc['fields']
				for f in fields:
					list_fields.append({'field_name': str(f).replace('"','').decode('utf-8'), 'channel': channel_id})
					count = count + 1

				#if no fields are valid the channel is removed from the list
				if count == 0:
					list_valid_channels.remove(dict)		
			else:
				print "Stream già presente"
		except UnicodeEncodeError:
			pass
		except KeyError:
			pass
		# What else?
		except:
			print(sys.exc_info()[0])
			continue

	return (list_valid_channels,list_fields)


def store_channels_in_db(list_channels):
	print "-----------------------------STORING CHANNEL ON DB----------------------------------"
	database = dbScraping.MyDB()

	for channel in list_channels:
		database.insert_channel(channel['channel_id'],channel['name'],channel['description'],"SparkFun")

	del database

def store_fields_in_db(list_fields):
	print "-----------------------------STORING FIELD ON DB----------------------------------"
	database = dbScraping.MyDB()

	for field in list_fields:
		database.insert_field(field['field_name'],field['channel'])

	del database

if __name__ == "__main__":
	
	maxP = int(sys.argv[1])
	thresh = int(sys.argv[2])
	

	myStreams = get_all_streams(maxP, thresh)

	(channels,fields) = get_stream_info(myStreams)

	store_channels_in_db(channels)
	store_fields_in_db(fields)
	

	