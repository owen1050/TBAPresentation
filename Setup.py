import tbapy

f = open("API_KEY.txt", "r")
key = f.read()
f.close()

tba = tbapy.TBA(key)

match = tba.match(key = "2024miket_qm14")

print(match["alliances"]["red"]["score"])