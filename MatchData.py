import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

matchKey = ""
match = tba.match(key = matchKey)

print(match["alliances"]["red"]["score"])