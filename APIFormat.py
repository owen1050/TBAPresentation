import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)


#tba.team_events(team, [year], [simple/keys]) - Get a list of events a team has been to.

team = "frc8513"

events = tba.team_events(team, year = "2025", keys = True)

print(events)