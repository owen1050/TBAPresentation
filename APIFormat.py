import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

#tba.team_events(team, [year], [simple/keys]) - Get a list of events a team has been to.

team = "frc8513"
year = "2024"

team = tba.team_events(team)

print(team)