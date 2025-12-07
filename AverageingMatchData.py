import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

#Checking what a specific team did this match
team = "frc8513"
match = "2025njfla_qm2"

match = tba.match(match)
isOnRed = team in match["alliances"]["red"]["team_keys"]
teamPos = -1
teamEndGame = ""
alliance = "blue"
if(isOnRed):
	alliance = "red"

#index of team key is 0,1,2 so add one to make it 1, 2, 3
teamPos = match["alliances"][alliance]["team_keys"].index(team) + 1
teamEndGame = match["score_breakdown"][alliance]["endGameRobot" + str(teamPos)]


print(team, "Alliance:", alliance, teamPos, "\nEnd Game:", teamEndGame)	