import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

team = "frc5401"
year = "2025"

matches = tba.team_matches(team, year = year, simple = False)
print(matches[0])
totalScore = 0
numberOfMatches = len(matches)

for match in matches:
	isOnRed = team in match["alliances"]["red"]["team_keys"]
	if(isOnRed):
		totalScore = totalScore + match["score_breakdown"]["red"]["netAlgaeCount"] - match["score_breakdown"]["blue"]["wallAlgaeCount"]
	else:
		totalScore = totalScore + match["score_breakdown"]["blue"]["netAlgaeCount"]- match["score_breakdown"]["red"]["wallAlgaeCount"]

print("totalScore:" + str(totalScore))
print("numMatches:" + str(numberOfMatches))
print("avgScore:" + str((totalScore/numberOfMatches)))