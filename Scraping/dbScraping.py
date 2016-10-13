import MySQLdb
import sys

class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = MySQLdb.connect("localhost","tirocinioLAM","LAM1516!","TestTrainingSet" )
        self._db_cur = self._db_connection.cursor()

    def get_update(self, channel_id):
        query = u'Select count(*) From Channel Where Id="{}" '.format(channel_id)
        response = self._db_cur.execute(query)
        self._db_connection.commit()
        return self._db_cur.fetchone()[0]

    
    def insert_channel(self, chid,name,description,provenance):
        try:
            query = u'INSERT INTO Channel (Id,Name,Description,Provenance) VALUES("{}","{}","{}","{}")'.format(chid,name,description,provenance)
            response = self._db_cur.execute(query)
            self._db_connection.commit()
        except UnicodeEncodeError:
            pass
        except:
            print(sys.exc_info()[0])
            pass

    def insert_field(self, name,chid):
        try:
            query = u'INSERT INTO Field (Field_name,Channel_id) VALUES("{}","{}")'.format(name,chid)
            response = self._db_cur.execute(query)
            self._db_connection.commit()
        except UnicodeEncodeError:
            pass
        except:
            print(sys.exc_info()[0])
            pass

    def insert_tag(self,tag_name,channel_id):
        try:
            query = u'INSERT INTO TagChannel (Tag_name,Channel_id) VALUES("{}","{}")'.format(tag_name,channel_id)
            response = self._db_cur.execute(query)
            self._db_connection.commit()
        except UnicodeEncodeError:
            pass
        except:
            print(sys.exc_info()[0])
            pass

    def get_all_channels_id(self,provenance):
        try:            
            query = u'Select Id From Channel Where Provenance="{}"'.format(provenance)
            response = self._db_cur.execute(query)
            channels = self._db_cur.fetchall()
            self._db_connection.commit()
            return channels
        except UnicodeEncodeError:
            pass
        except:
            print(sys.exc_info()[0])
            pass

    def __del__(self):
        self._db_connection.close()