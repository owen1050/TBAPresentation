import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

matchKey = "2025paphi_sf5m1"
match = tba.match(key = matchKey)

print(match)