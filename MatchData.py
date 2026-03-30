import tbapy

import pickle

def getWinnersFromEventCode(code):
	winners = []
	awards = tba.event_awards(code)
	for award in awards:
		if(int(award["award_type"]) == 1):
			for team in award["recipient_list"]:
				winners.append(team["team_key"])
	return winners

def getEventCodesFromYear(yearIn):
	events = tba.events(year = yearIn)
	ret = []
	for event in events:
		ret.append(event["key"])
	return ret

def getEventWinnerListMap(year):
	eventToWinnerList = {}
	events = getEventCodesFromYear(year)
	for event in events:
		eventToWinnerList[event] = getWinnersFromEventCode(event)

	return eventToWinnerList

def generateAllEventsToWinnerMaps():
	years = []
	for year in range(1992, 2027):
		years.append(getEventWinnerListMap(year))
		print(year)
	return years




f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

data = generateAllEventsToWinnerMaps()

with open('dataafter4.pkl', 'wb') as file:
	pickle.dump(data, file)

print(data)


