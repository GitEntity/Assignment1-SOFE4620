# Author: Devante Wilson
# Date: 7/28/2018
# Description: Connect to the API site in order to scrape data intended for writing to .csv file.
import http.client
import json
import pandas as pd

# setup the connection to the api site
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '49545ccc5fa148e889e3cc4a7f7d6113', 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions/446/leagueTable', None, headers )
# read and decode the json data in the response
response = json.loads(connection.getresponse().read().decode())

# output the list to the console
print(response)

# write DataFrame to a comma seperated values (csv) file
data = pd.DataFrame(response)
data.to_csv('PremierLeague.csv', index=False)
