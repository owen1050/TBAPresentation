import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

team = "frc8513"
year = "2025"

matches = tba.team_matches(team, year = year, simple = True)

totalScore = 0
numberOfMatches = len(matches)

for match in matches:
	isOnRed = team in match["alliances"]["red"]["team_keys"]
	if(isOnRed):
		totalScore = totalScore + match["alliances"]["red"]["score"]
	else:
		totalScore = totalScore + match["alliances"]["blue"]["score"]

print("totalScore:" + str(totalScore))
print("numMatches:" + str(numberOfMatches))
print("avgScore:" + str((totalScore/numberOfMatches)))