import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

#https://www.thebluealliance.com/match/2024njfla_qm18
#8513 and 1218 climbed, 8513 trapped (Would have been earliest double trap in world)
team = "frc8513"
match = "2024njfla_qm18"

match = tba.match("2024njfla_qm18")
isOnRed = team in match["alliances"]["red"]["team_keys"]
teamPos = -1
teamEndGame = ""
trapped = False
alliance = "blue"
if(isOnRed):
	alliance = "red"

#index of team key is 0,1,2 so add one to make it 1, 2, 3
teamPos = match["alliances"][alliance]["team_keys"].index(team) + 1
teamEndGame = match["score_breakdown"][alliance]["endGameRobot" + str(teamPos)]
trapped = match["score_breakdown"][alliance]["trap" + teamEndGame]


print(team, "Alliance:", alliance, teamPos, "\nClimbed:", teamEndGame, "Trapped:", trapped)	