import MySQLdb
import urllib
import string

def ip_to_location(ip_str):
    """
    ip_to_location: Looks up the location information of an IP address.
    Uses ip database from http://hostip.info and publicly available zip code database pulled from
    http://scripts.ringsworld.com/calculators/zipcode-1.1.0/
    
    @ip_str: IPv4 address in "aaa.bbb.ccc.ddd" form.
    
    Outputs a tuple in (city, state, Ip lat, lng) form.
    Return ("", "", None, None, None) if nothing is found.
    """
    a,b,c,d = ip_str.split(".")
    conn = MySQLdb.connect (host = 'localhost',
                            user = 'solar',
                            passwd = 's0l4r',
                            db = 'hostip')
    cursor = conn.cursor()
    cursor.execute("SELECT name, state, lat, lng FROM cityByCountry WHERE (city, country) = (select city, country from ip4_"+a+" where b = "+b+" and c = "+c+")")
    if cursor.rowcount == 0:
        return ("", "", None, None, None)
    name, state, lat, lng = cursor.fetchone()
    city = ",".join(urllib.unquote(name).split(',')[:-1])
    state = urllib.unquote(name).split(', ')[-1].strip()
    
    cursor.execute("SELECT zip_code FROM zip_code WHERE city = '"+string.upper(city)+"' AND state_prefix = '"+state+"'");
    
    zip_code = None
    if cursor.rowcount > 0:
        zip_code = str(cursor.fetchone()[0]).rjust(5, "0")
        
    return (city, state, zip_code, lat, lng)
    
def city_to_latlng(city, state):
    """
    city_to_latlng: Looks up the latitude and longitude of a city.
    
    Outputs a tuple in (lat, lng) form.
    Returns False is no such city is found.
    """
    conn = MySQLdb.connect (host = 'localhost',
                            user = 'solar',
                            passwd = 's0l4r',
                            db = 'hostip')
    cursor = conn.cursor()
    cursor.execute("SELECT lattitude, longitude FROM zip_code WHERE (city, state_prefix) = ('"+string.upper(city)+"','"+string.upper(state)+"')")
    
    if cursor.rowcount == 0:
        return False
    lat, lng = cursor.fetchone()
    
    return (lat, lng)
    
def zip_to_latlng(zip):
    """
    city_to_latlng: Looks up the latitude and longitude of a zip code.

    Outputs a tuple in (lat, lng) form.
    Returns False is no such zip is found.
    """
    conn = MySQLdb.connect (host = 'localhost',
                            user = 'solar',
                            passwd = 's0l4r',
                            db = 'hostip')
    cursor = conn.cursor()
    cursor.execute("SELECT lattitude, longitude FROM zip_code WHERE zip_code = "+str(zip))

    if cursor.rowcount == 0:
        return False
    lat, lng = cursor.fetchone()

    return (lat, lng)
