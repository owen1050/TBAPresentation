import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

matchKey = "2025njfla_f1m2"
match = tba.match(key = matchKey)

print(match)