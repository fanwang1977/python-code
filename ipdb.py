import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print(rec)
    print('[*] Target: ' + tgt + ' Geo-located. ')
    print('[+] ' + str(city) + ', ' + str(country))
    print('[+] Latitude: ' + str(lat) + ', Longitude: ' + str(long))
tgt = '114.114.114.114'
printRecord(tgt)

