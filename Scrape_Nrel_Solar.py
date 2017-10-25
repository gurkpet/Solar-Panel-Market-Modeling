solar_radiation = []
codes = []
for i, zipcode in enumerate(zipcodesx):
    this_url = 'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key='+apikey+'&address='+zipcode
    with urllib.request.urlopen(this_url) as url:
        data = json.loads(url.read().decode())
    
    
    print("{} of {} zipcodes processed: {}".format(i+1, len(zipcodes), zipcode), end = '\r')
    if 'annual' in data['outputs']['avg_dni']:
        solar_radiation.append(data['outputs']['avg_dni']['annual'])
    else:
        solar_radiation.append('error')
    codes.append(zipcode)
    
    if ((i+1) % 900) == 0:
        #Rest for 1 hour
        print('Resting for 1 hour before continuing, currently on zipcode no. {}'.format(i), end = '\r')
        time.sleep(3600) 
        
df = pd.DataFrame()
df['zipcode'] = codes
df['solar_radiation'] = solar_radiation
df.to_csv('Scraped_Solar.csv', index = False, header = True)