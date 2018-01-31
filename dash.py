""" dash.py - my Bus Time Dashboard """

import config
import requests
import simplejson as json
import csv

baseurl=config.baseurl + 'getpredictions'
apikey=config.apikey


def handle_error(errmsg):
    for item in errmsg:
        print("Error for Stop: %s" %  item['stpid'])
        # print("Route:          %s" %  item['rt'])
        # print("Message:        %s" %  item['msg'])
        # print("Skipping. . . ")
        print(item)

def parse_response(response):
    for message in response.values():
        if 'error' in message.keys():
             handle_error(message['error'])
        else:
            for prediction in message.values():
                for stop in prediction:
                    print("Stop Name: %s" % stop['stpnm'])
                    print("Route:     %s" % stop['rt'])
                    print("Vehicle:   %s" % stop['vid'])
                    print("Delayed:   %s" % stop['dly'])
                    print("ETA:       %s minutes" % stop['prdctdn'])
                    print()

def main(): 
    with open('routes.csv') as routesfile:
        readCSV = csv.DictReader(routesfile)
        for row in readCSV:
          #print("Route: %s  Stop: %s Direction: %s" % (row['rt'], row['stpid'], row['dir']))
          del row['dir']  # we don't need the direction for stop predction
          row.update([('format', 'json'), ('key', apikey), ('rtpidatafeed', 'Port Authority Bus')])
          r = requests.get(baseurl, params=row)
          answer = json.loads(r.text)
          parse_response(answer)

    
if __name__ == '__main__':
    main()    
