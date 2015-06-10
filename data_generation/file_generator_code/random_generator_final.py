import random
import time

#this is for finding distance between two locations using
#their respective longitutde and latitude
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    mi = km/1.609344
    return mi

print int(haversine(40.5249235, -75.2875279647195,38.3010487, -88.9344303))
#for time generation
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)
    #return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

def randomTime(start, end, prop):
    return strTimeProp(start, end, '%I:%M %p', prop)
#type of truck method

def truckType(number):
	dict={1: 'F',2:'FT',3:'F',4:'V',5:'F',6:'FD',7:'F'}
	return dict[number]	
my_date=randomDate("1/1/2005", "1/1/2015", random.random())
my_time=randomTime("12:00 PM", "12:00 AM", random.random())
origin=random.choice(open("complete_city.csv").readlines()).strip()
destination=random.choice(open("complete_city.csv").readlines()).strip()
location_origin = geolocator.geocode(origin,exactly_one=True,timeout=10)
location_destination = geolocator.geocode(destination,exactly_one=True,timeout=10)
origin_long_lat=(location_origin.latitude,location_origin.longitude)
destination_long_lat=(location_destination.latitude,location_destination.longitude)
#print origin_long_lat
trip= int((vincenty(origin_long_lat,destination_long_lat).miles))
if(origin != destination):
	print "\""+my_time+"\","+"\""+my_date+"\","+"\""+truckType(random.randint(1,7))+"\","+"\""+"F"+"\","+"\""+" "+"\","+"\""+origin+"\","+"\""+str(trip)+"\","+"\""+destination+"\","+"\""+" "+"\","+"\""+"(111) 111-1111"+"\","+"\""+str(random.randint(80,100))+"\","+"\""+str(random.randint(30,40))+"\","+"\""+" "+"\","+"\""+str(random.randint(10,45))+"\","+"\""+"Company XXX"+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+"R"+"\","+"\""+"A"+"\""

#print "\""+my_time+"\","+"\""+my_date+"\","+"\""+truckType(random.randint(1,7))+"\","+"\""+"F"+"\","+"\""+" "+"\","+"\""+random.choice(open("complete_city.csv").readlines()).strip()+"\","+"\""+str(random.randint(100,2000))+"\","+"\""+random.choice(open("complete_city.csv").readlines()).strip()+"\","+"\""+" "+"\","+"\""+"(111) 111-1111"+"\","+"\""+str(random.randint(80,100))+"\","+"\""+str(random.randint(30,40))+"\","+"\""+" "+"\","+"\""+str(random.randint(10,45))+"\","+"\""+"Company XXX"+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+"R"+"\","+"\""+"A"+"\""
