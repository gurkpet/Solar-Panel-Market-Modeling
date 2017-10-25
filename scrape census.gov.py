#lists to hold the data being scraped
zipcode = []
population = []
medianage = []
medianincome = []
pplinownerocc = []
#iterate through every entry in the scrape, each entry being one zip code
for code in data:
    #save the various data to lists
    zipcode.append(code['zip code tabulation area'])
    population.append(code['B25008_001E'])
    medianage.append(code['B01002_001E'])
    medianincome.append(code['B25119_001E'])
    pplinownerocc.append(code['B25008_002E'])

#save the lists to a dataframe
df = pd.DataFrame()
df['zipcode'] = zipcode
df['population'] = population
df['medianage'] = medianage
df['medianincome'] = medianincome
df['pplinownerocc'] = pplinownerocc
#calulate a percentage of people living in their own homes
df['pctownocc'] = round(df.pplinownerocc/df.population, 2)
#drop nan values for good measure
df.dropna(inplace = True)
#save the scraped data
df.to_csv('scraped_from_census.csv',index = False, header = True)