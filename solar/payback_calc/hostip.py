import MySQLdb
import urllib
import string

def hostip(ip_str):
    """
    hostip: Wrapper for ip geolocation database
    Uses database from http://hostip.info
    
    @ip_str: IPv4 address in "aaa.bbb.ccc.ddd" form.
    
    Outputs a tuple in (city, state, lat, lng) form.
    Return ("", "", None, None) if nothing is found.
    """
    a,b,c,d = ip_str.split(".")
    conn = MySQLdb.connect (host = 'localhost',
                            user = 'solar',
                            passwd = 's0l4r',
                            db = 'hostip')
    cursor = conn.cursor()
    cursor.execute("SELECT name, state, lat, lng FROM cityByCountry WHERE (city, country) = (select city, country from ip4_"+a+" where b = "+b+" and c = "+c+")")
    if cursor.rowcount == 0:
        return ("", "", None, None)
    name, state, lat, lng = cursor.fetchone()
    city = ",".join(urllib.unquote(name).split(',')[:-1])
    state = urllib.unquote(name).split(', ')[-1].strip()
    
    cursor.execute("SELECT zip_code FROM zip_code WHERE city = '"+string.upper(city)+"' AND state_prefix = '"+state+"'");
    zip_code = str(cursor.fetchone()[0]).rjust(5, "0")
    return (city, state, zip_code, lat, lng)
    
    
