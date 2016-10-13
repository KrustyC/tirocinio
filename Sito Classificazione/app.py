# -*- coding: UTF-8 -*-

from flask import Flask, send_file, request
import MySQLdb
import json

app = Flask(__name__)
limit = 2000

relevantKeys = ['Dust_Level','Gas_Level','Brightness','Power','UV','Heat_Index','Pressure', 'Rain_Index', 'Radiation', 'Temperature',
   				'Humidity', 'Wind_Direction', 'Wind_Speed']

@app.route("/")
def index():
    return send_file("templates/index.html")
	
@app.route('/channels', methods=['GET'])
def getChannels():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()


	dict = []
	for item in data:
		link = ""
		if(item[6] == "ThingSpeak"):
			link =  'https://thingspeak.com/channels/' + str(item[0])
		else:
			link =  'https://data.sparkfun.com/streams/' + item[0]		
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'link':link})

	return json.dumps(dict) 

@app.route('/channelsClass', methods=['GET'])
def getChannelsClass():
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 WHERE f.Class = "Class" \
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		link = ""
		if(item[6] == "ThingSpeak"):
			link =  'https://thingspeak.com/channels/' + str(item[0])
		else:
			link =  'https://data.sparkfun.com/streams/' + item[0]
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'link':link})


	return json.dumps(dict) 

@app.route('/channelsSet', methods=['GET'])
def getChannelsSet():
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance, f.SetType \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		link = ""
		if(item[6] == "ThingSpeak"):
			link =  'https://thingspeak.com/channels/' + str(item[0])
		else:
			link =  'https://data.sparkfun.com/streams/' + item[0]
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'link':link,'set':item[7]})


	return json.dumps(dict) 

@app.route('/channelsBySet/<setType>', methods=['GET'])
def getChannelsBySet(setType):
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance, f.SetType \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 WHERE f.SetType = "{}" \
			 LIMIT {}'.format(setType,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'set':item[7]})


	return json.dumps(dict) 


@app.route('/channelsSetByClass/<classe>', methods=['GET'])
def getChannelsSetByClass(classe):
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance, f.SetType \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 WHERE f.Class="{}" \
			 LIMIT {}'.format(classe,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'set':item[7]})

	return json.dumps(dict) 


@app.route('/getClassStream/<className>', methods=['GET'])
def getChannelsClassStream(className):
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT s.Id,s.Name,s.Description,f.Id,f.Field_name,f.Class, s.Provenance \
			 FROM Channel AS s JOIN Field AS f ON s.Id = f.Channel_id\
			 WHERE f.Class = "{}" \
			 LIMIT {}'.format(className,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		link = ""
		if(item[6] == "ThingSpeak"):
			link =  'https://thingspeak.com/channels/' + str(item[0])
		else:
			link =  'https://data.sparkfun.com/streams/' + item[0]
		dict.append({'channel_id': item[0],'channel_name':item[1],'channel_description':item[2],'field_id':item[3],'field_name':item[4],'field_class':item[5],'provenance':item[6],'link':link})


	return json.dumps(dict) 

	
@app.route('/deleteField/<int:fieldId>', methods=['DELETE'])
def delete_entry(fieldId):
	
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'DELETE  FROM Field\
			 WHERE id = {} '.format(fieldId)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	return "Delete success"


@app.route('/updateClass', methods=['POST'])
def update_class():
	
	field = request.form['field']
	classe = request.form['classe']
    
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'UPDATE Field\
			 SET Class = "{}"\
			 WHERE id = {} '.format(classe,field)

	
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()
	
	return "Update success"

@app.route('/updateSet', methods=['POST'])
def update_set():
	
	field = request.form['field']
	new_set = request.form['set']
    
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'UPDATE Field\
			 SET SetType = "{}"\
			 WHERE id = {} '.format(new_set,field)

	
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()
	
	return "Update success"





@app.route('/getInfo', methods=['GET'])
def get_info():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()

	#Numero di stream globalmente presenti
	query1 = 'SELECT count(*) AS "Stream Totali"\
	FROM Channel JOIN Field on Channel.Id = Field.Channel_id'

	cur.execute(query1)
	totCount = cur.fetchone()[0]

	#Numero di stream provenienti da Sparkfun
	query2 = 'SELECT count(*) AS "Stream Totali"\
	FROM Channel JOIN Field on Channel.Id = Field.Channel_id\
	WHERE Channel.Provenance = "SparkFun" '

	cur.execute(query2)
	sfCount = cur.fetchone()[0]	

	#Numero di stream provenienti da ThingSPeak
	query3 = 'SELECT count(*) AS "Stream Totali"\
	FROM Channel JOIN Field on Channel.Id = Field.Channel_id\
	WHERE Channel.Provenance = "ThingSpeak" '

	cur.execute(query3)
	tsCount = cur.fetchone()[0]

	#Numero di stream ancora già classificati
	query4 = 'SELECT count(*) AS "Stream Totali"\
			 FROM Channel JOIN Field on Channel.Id = Field.Channel_id\
			 WHERE Field.Class <> "Class"'

	cur.execute(query4)
	classifiedCount = cur.fetchone()[0]


   	query5 = query = 'SELECT count(*)\
			 FROM Field\
			 WHERE Class in ("Dust_Level","Gas_Level","Brightness","Power","UV","Heat_Index","Pressure", "Rain_Index", "Radiation", "Temperature",\
   				"Voltage", "Current", "Humidity", "Wind_Direction", "Wind_Speed")'

	cur.execute(query5)
	relevantCount = cur.fetchone()[0]


	testSet = 'SELECT count(*) \
			 FROM Field \
			 WHERE Field.SetType = "Test"'

	cur.execute(testSet)
	testCount = cur.fetchone()[0]

	trainingSet = 'SELECT count(*) \
			 FROM Field \
			 WHERE Field.SetType = "Training"'


	cur.execute(trainingSet)
	trainingCount = cur.fetchone()[0]


	info = {'totCount' : totCount, 'sfCount':sfCount,'tsCount':tsCount,'classifiedCount':classifiedCount,'relevantCount':relevantCount,'testCount':testCount,'trainingCount':trainingCount}

	db.commit()
	db.close()
	
	return json.dumps(info)


@app.route('/classCount/<className>', methods=['GET'])
def classCount(className):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	
	query = 'SELECT count(*) AS "Stream Totali"\
			 FROM Channel JOIN Field on Channel.Id = Field.Channel_id\
			 WHERE Field.Class = "{}"'.format(className)

	cur.execute(query)
	data = cur.fetchone()
	
	db.commit()
	db.close()

	return json.dumps({u'streamClasse': data[0]}) 


@app.route('/getTags/<channelId>', methods=['GET'])
def getTags(channelId):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	
	query = 'SELECT Tag_name\
			 FROM TagChannel\
			 WHERE Channel_id = "{}"'.format(channelId)

	cur.execute(query)
	data = cur.fetchall()
	
	db.commit()
	db.close()

	dict = []
	if(len(data) > 0):
		for tag in data:
			dict.append(tag[0])
		return json.dumps(dict) 
	else: 
		return json.dumps(['Non ci sono tag per questo channel']) 


@app.route('/getClassification', methods=['GET'])
def getClassification():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Field_name,Field_class,Channel_name,Channel_description,Attributed_class,Distance,Field_id,Channel_id \
			 FROM Classification\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'field_name': item[0],'field_class':item[1],'channel_name':item[2],'channel_description':item[3],'attributed_class':item[4],'distance':item[5],'field_id':item[6],'channel_id':item[7]})

	
	return json.dumps(dict) 


@app.route('/getClassificationByNumber/<number>', methods=['GET'])
def getClassificationByNumber(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Field_name,Field_class,Channel_name,Channel_description,Attributed_class,Distance,Field_id,Channel_id \
			 FROM Classification\
			 WHERE Number={} \
			 LIMIT {}'.format(number,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'field_name': item[0],'field_class':item[1],'channel_name':item[2],'channel_description':item[3],'attributed_class':item[4],'distance':item[5],'field_id':item[6],'channel_id':item[7]})

	
	return json.dumps(dict) 

@app.route('/getClassificationRelevantByNumber/<number>', methods=['GET'])
def getClassificationRelevantByNumber(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Field_name,Field_class,Channel_name,Channel_description,Attributed_class,Distance,Field_id,Channel_id \
			 FROM ClassificationRelevant\
			 WHERE Number={} \
			 LIMIT {}'.format(number,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'field_name': item[0],'field_class':item[1],'channel_name':item[2],'channel_description':item[3],'attributed_class':item[4],'distance':item[5],'field_id':item[6],'channel_id':item[7]})

	
	return json.dumps(dict) 

@app.route('/getMetrics', methods=['GET'])
def getMetrics():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM Metric\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	return json.dumps(dict) 

@app.route('/getMetricsRelevant', methods=['GET'])
def getMetricsRelevant():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM MetricRelevant\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	return json.dumps(dict) 


@app.route('/getMetricsByNumber/<number>', methods=['GET'])
def getMetricsByNumber(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM Metric\
			 WHERE Number={}\
			 LIMIT {}'.format(number,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	return json.dumps(dict) 

@app.route('/getMetricsRelevantByNumber/<number>', methods=['GET'])
def getMetricsRelevantByNumber(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM MetricRelevant\
			 WHERE Number={}\
			 LIMIT {}'.format(number,limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	return json.dumps(dict) 

def getMedia(dict):
	tot_recall = 0
	tot_precision = 0
	tot_fmeasure = 0

	for item in dict:
		tot_recall += item['recall']
		tot_precision += item['precision']
		tot_fmeasure += item['f_measure']

	tot_recall = '%.6f' % round((tot_recall / 10), 6)
	tot_precision = '%.6f' % round((tot_precision / 10), 6)
	tot_fmeasure = '%.6f' % round((tot_fmeasure / 10), 6)

	dict.append({'class': 'Media','recall':tot_recall,'precision':tot_precision,'f_measure':tot_fmeasure})

	return dict


@app.route('/getTotalMetrics', methods=['GET'])
def getTotalMetrics():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM Metric\
			 WHERE Class="Totale" OR Class="Relevant"\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	dict = getMedia(dict)
	return json.dumps(dict) 

@app.route('/getTotalRelevantMetrics', methods=['GET'])
def getTotalRelevantMetrics():
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()
	query = 'SELECT Class,Recall,Precisions,F_measure,M_timestamp\
			 FROM MetricRelevant\
			 WHERE Class="Totale"\
			 LIMIT {}'.format(limit)
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:	
		dict.append({'class': item[0],'recall':item[1],'precision':item[2],'f_measure':item[3],'timestamp':item[4].strftime('%Y-%m-%d %H:%M:%S')})

	dict = getMedia(dict)
	return json.dumps(dict) 


def getTotal(dict):
	totTemp = 0
	totGas = 0
	totBrightness = 0
	totHum = 0
	totWinDir = 0
	totWinSpeed = 0
	totRainIndex = 0
	totDust = 0
	totHeat = 0
	totPres = 0
	totPow = 0
	totRad = 0
	totUV = 0

	for item in dict:
		totTemp += item['Temperature']
		totGas += item['Gas_Level']
		totBrightness += item['Brightness']
		totHum += item['Humidity']
		totWinDir += item['Wind_Direction']
		totWinSpeed += item['Wind_Speed']
		totRainIndex += item['Rain_Index']
		totDust += item['Dust_Level']
		totHeat += item['Heat_Index']
		totPres += item['Pressure']
		totPow += item['Power']
		totRad += item['Radiation']
		totUV += item['UV']

	dict.append({'Temperature': totTemp,'Gas_Level':totGas,'Brightness':totBrightness,'Humidity':totHum,'Wind_Direction':totWinDir,
			'Wind_Speed': totWinSpeed,'Rain_Index':totRainIndex,'Dust_Level':totDust,'Heat_Index':totHeat,
			'Pressure':totPres,'Power':totPow,'Radiation':totRad,
			'UV':totUV,'Classe':"WTotale"})

	return dict

def getTotalAll(dict):
	totTemp = 0
	totGas = 0
	totBrightness = 0
	totHum = 0
	totWinDir = 0
	totWinSpeed = 0
	totRainIndex = 0
	totDust = 0
	totHeat = 0
	totPres = 0
	totPow = 0
	totRad = 0
	totUV = 0
	totVoltage = 0
	totDewpoint = 0
	totCurrent = 0
	totDistance= 0
	totEnergy = 0
	totCPU = 0
	totCapacity = 0
	totPrice = 0
	totGeolocalization = 0
	totPH = 0
	totBattery = 0
	totColour = 0
	totHeight = 0
	totRate = 0
	totLQI  = 0
	totCount = 0
	totMemory = 0
	totTime = 0
	totMotion = 0
	totUV = 0
	totRSSI = 0

	for item in dict:
		totTemp += item['Temperature']
		totGas += item['Gas_Level']
		totBrightness += item['Brightness']
		totHum += item['Humidity']
		totWinDir += item['Wind_Direction']
		totWinSpeed += item['Wind_Speed']
		totRainIndex += item['Rain_Index']
		totDust += item['Dust_Level']
		totHeat += item['Heat_Index']
		totPres += item['Pressure']
		totPow += item['Power']
		totRad += item['Radiation']
		totUV += item['UV']
		totVoltage += item['Voltage']
		totDewpoint += item['Dewpoint']
		totCurrent += item['Current']
		totDistance+= item['Distance']
		totEnergy += item['Energy']
		totCPU += item['CPU_Usage']
		totCapacity += item['Capacity']
		totPrice += item['Price']
		totGeolocalization += item['Geolocalization']
		totPH += item['PH']
		totBattery += item['Battery_Level']
		totColour += item['Colour']
		totHeight += item['Height']
		totRate += item['Rate']
		totLQI  += item['LQI']
		totCount += item['Count']
		totMemory += item['Memory']
		totTime += item['Time']
		totMotion += item['Motion']
		totUV += item['UV']
		totRSSI += item['RSSI']

	dict.append({'Temperature': totTemp,'Gas_Level':totGas,'Brightness':totBrightness,'Humidity':totHum,'Wind_Direction':totWinDir,
			'Wind_Speed': totWinSpeed,'Rain_Index':totRainIndex,'Dust_Level':totDust,'Heat_Index':totHeat,
			'Pressure':totPres,'Power':totPow,'Radiation':totRad,'UV':totUV,
			'Voltage':totVoltage,'Dewpoint':totDewpoint,'Current':totCurrent,'Distance':totDistance,'Energy':totEnergy,
			'CPU_Usage':totCPU,'Capacity':totCapacity,'Price':totPrice,'Geolocalization':totGeolocalization,
			'PH':totPH,'Battery_Level':totBattery,'Colour':totColour,'Height':totHeight,'Rate':totRate,
			'LQI':totLQI,'Count':totCount,'Memory':totMemory,'Time':totTime,'Motion':totMotion,
			'UV':totUV,'RSSI':totRSSI,'Classe':"WTotale"})

	return dict

@app.route('/getConfusionMatrix/<number>', methods=['GET'])
def getConfusionMatrix(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()

	query = 'SELECT Temperature,Gas_Level,Brightness,Humidity,Wind_Direction,Wind_Speed,Rain_Index,\
			Dust_Level,Heat_Index,Pressure,Power,Radiation,UV,Class\
			FROM ConfusionMatrixRelevant\
			WHERE Number={}'.format(int(number))
	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		tot = 0
		for i in range(0,13):
			tot += item[i]
		dict.append({'Temperature': item[0],'Gas_Level':item[1],'Brightness':item[2],'Humidity':item[3],'Wind_Direction':item[4],
			'Wind_Speed': item[5],'Rain_Index':item[6],'Dust_Level':item[7],'Heat_Index':item[8],
			'Pressure':item[9],'Power':item[10],'Radiation':item[11],
			'UV':item[12],'Classe':item[13],'Totale':tot})


	dict = getTotal(dict)
	return json.dumps(dict) 


@app.route('/getConfusionMatrixAll/<number>', methods=['GET'])
def getConfusionMatrixAll(number):
	db = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
	cur = db.cursor()


	query = 'SELECT Temperature,Gas_Level,Brightness, Voltage,Humidity,Wind_Direction,Wind_Speed,Rain_Index,\
			Dust_Level,Heat_Index,Dewpoint,Current,Distance,Energy,CPU_Usage,Capacity,Price,Geolocalization,Pressure,PH,Power,Radiation,\
			Battery_Level,Colour,Height,Rate,LQI,Count,Memory,Time,Motion,UV,RSSI,Class\
			FROM ConfusionMatrix\
			WHERE Number={}'.format(number)

	cur.execute(query)
	data = cur.fetchall()
	db.commit()
	db.close()

	dict = []
	for item in data:
		tot = 0
		for i in range(0,33):
			tot += item[i]	
		dict.append({'Temperature': item[0],'Gas_Level':item[1],'Brightness':item[2],'Voltage':item[3],'Humidity':item[4],'Wind_Direction':item[5],
			'Wind_Speed': item[6],'Rain_Index':item[7],'Dust_Level':item[8],'Heat_Index':item[9],'Dewpoint':item[10],
			'Current': item[11],'Distance':item[12],'Energy':item[13],'CPU_Usage':item[14],'Capacity':item[15],'Price':item[16],
			'Geolocalization': item[17],'Pressure':item[18],'PH':item[19],'Power':item[20],'Radiation':item[21],'Battery_Level':item[22],
			'Colour': item[23],'Height':item[24],'Rate':item[25],'LQI':item[26],'Count':item[27],'Memory':item[28],
			'Time': item[29],'Motion':item[30],'UV':item[31],'RSSI':item[32],'Classe':item[33],'Totale':tot})

	dict = getTotalAll(dict)
	return json.dumps(dict) 




if __name__ == '__main__':
    app.run(debug=True)

if __name__ == __main__:
    app.run(debug=True)
