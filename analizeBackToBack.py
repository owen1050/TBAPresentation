import pickle

backToBack = []

backToBackYearTeams = {}

with open('dataafter4.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

for i in range(len(loaded_data)):
    year = loaded_data[i]
    teamsBTB = []
    yearInt = 0
    for event in year:
        yearInt = int(event[0:4])
        eventMinusYear = event[4:]
        try:
            teamsWonThis = year[event]
            teamsWonNext = loaded_data[i+1][str(yearInt + 1) + eventMinusYear]
            teamsWonNextNext = loaded_data[i+2][str(yearInt + 2) + eventMinusYear]
            teamsWonNextNextNext = loaded_data[i+3][str(yearInt + 3) + eventMinusYear]
            teamsWonNextNextNextNext = loaded_data[i+4][str(yearInt + 4) + eventMinusYear]
            for team in teamsWonThis:
                if(team in teamsWonNext and team in teamsWonNextNext and team in teamsWonNextNextNext and team in teamsWonNextNextNextNext):
                    backToBack.append((team, eventMinusYear, yearInt))
                    teamsBTB.append(team)
            #print(eventMinusYear, teamsWonThis, teamsWonNext)
        except:
            pass
    backToBackYearTeams[yearInt] = teamsBTB


for year in backToBackYearTeams:
    teamsAlreadySeen = []
    for team in backToBackYearTeams[year]:
        if(team in teamsAlreadySeen):
            print(team, year)
        teamsAlreadySeen.append(team)

#print(backToBackYearTeams)
#results of analysis https://docs.google.com/spreadsheets/d/1gpwu8wPT218e3WQY1XekahS6zwPsodvSDgcMBg6xwn4/edit?usp=sharing