import tbapy


def getAverageScore(team, year):

	matches = tba.team_matches(team, year = year, simple = True)

	totalScore = 0
	numberOfMatches = len(matches)

	for match in matches:
		isOnRed = team in match["alliances"]["red"]["team_keys"]
		if(isOnRed):
			totalScore = totalScore + match["alliances"]["red"]["score"]
		else:
			totalScore = totalScore + match["alliances"]["blue"]["score"]

	if(numberOfMatches == 0):
		return 0
	return totalScore/numberOfMatches

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

year = "2024"
district = "fma"

teams = tba.district_teams(year + district, keys = True)
print("Got a list of " + str(len(teams)) + " teams")

for team in teams[0:20]:
	print(team + ":" + str(getAverageScore(team, year)))





