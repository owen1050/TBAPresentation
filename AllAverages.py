import tbapy


def getAverageScore(team, year):

	matches = tba.team_matches(team, year = year, simple = False)

	totalScore = 0
	numberOfMatches = len(matches)

	for match in matches:
		isOnRed = team in match["alliances"]["red"]["team_keys"]
		if(isOnRed):
			totalScore = totalScore + match["score_breakdown"]["red"]["netAlgaeCount"] - match["score_breakdown"]["blue"]["wallAlgaeCount"]
		else:
			totalScore = totalScore + match["score_breakdown"]["blue"]["netAlgaeCount"]- match["score_breakdown"]["red"]["wallAlgaeCount"]

	if(numberOfMatches == 0):
		return 0
	return totalScore/numberOfMatches

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

year = "2025"
district = "fma"

teams = tba.district_teams(year + district, keys = True)
print("Got a list of " + str(len(teams)) + " teams")

print(teams)





