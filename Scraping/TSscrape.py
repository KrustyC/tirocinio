#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import json
import sys
from urllib2 import HTTPError
import dbScraping

from datetime import datetime, timedelta
import requests

keyArray = ['description', 'elevation', 'name', 'created_at', 'updated_at', 'longitude', 'latitude', 'last_entry_id', 'id', 'tags', 'metadata', 'url']


def trim_string(string):
	string = string.replace('"','')
	string = string.replace("'","")
	return string

def get_metadata_channels_and_fields(begin, end):
	print "-----------------------------GETTING THE METADATA----------------------------------"
	
	list_valid_channels = []
	fields = []
	for i in range(begin, end):	
		print "Evaluating stream " + str(i) + "..."
		ff = "https://thingspeak.com/channels/" + str(i) + "/feed.json"
		f = ""
		jj = ""
		
		try:
			# Parse the JSON from the page and get the root element
			f = urlopen('https://thingspeak.com/channels/' + str(i) + '/feed.json').read().decode("utf-8")
			jj = json.loads(f)  # string to json
			chan = jj['channel']  # metadata
			# Get the data fields (database mode only)
			channel_id = trim_string(str(chan['id'])).decode("utf-8")

			database = dbScraping.MyDB()
			response = database.get_update(channel_id)
			del database
			
			if response == 0:
				channel_name = trim_string(str(chan['name'])).decode("utf-8")
				channel_description = trim_string(str(chan['description'])).decode("utf-8")


				dict = {'channel_id': channel_id,'name':channel_name,'description':channel_description}
				list_valid_channels.append(dict)
				
				count = 0
				for item in chan.keys():
					if item.startswith('field'):  # we found a field
						fields.append({'field_name': str(chan[item]).replace('"','').decode('utf-8'), 'channel': channel_id})
						count = count + 1

				#if no fields are valid the channel is removed from the list
				if count == 0:
					list_valid_channels.remove(dict)		
			else:
				print "Stream già presente"
						
			
		# "channel" field not found
		except KeyError:
			print "HTTP 404 Response"
			
		# We pass those 'cause we might have some private channels	
		except HTTPError:
			pass
		
		except TypeError:
			print "This is a Private Channel..."
			
		except UnicodeEncodeError:
			pass

		# What else?
		except:
			print(sys.exc_info()[0])

	return (list_valid_channels,fields)
	

def store_channels_in_db(list_channels):
	print "-----------------------------STORING CHANNEL ON DB----------------------------------"
	database = dbScraping.MyDB()

	for channel in list_channels:
		try:
			database.insert_channel(channel['channel_id'],channel['name'],channel['description'],"ThingSpeak")
		except UnicodeEncodeError:
			pass
		except dbScraping.MySQLdb.IntegrityError:
			pass
		except:
			print(sys.exc_info()[0])
			pass

	del database

def store_fields_in_db(list_fields):
	print "-----------------------------STORING FIELD ON DB----------------------------------"
	database = dbScraping.MyDB()

	for field in list_fields:
		try:
			database.insert_field(field['field_name'],field['channel'])
		except UnicodeEncodeError:
			pass
		except dbScraping.MySQLdb.IntegrityError:
			pass
		except:
			print(sys.exc_info()[0])
			pass

	del database


if __name__ == "__main__":
	
	beg = int(sys.argv[1])
	fin = int(sys.argv[2])
	
	(channels,fields) = get_metadata_channels_and_fields(beg, fin)

	store_channels_in_db(channels)
	store_fields_in_db(fields)
	

	