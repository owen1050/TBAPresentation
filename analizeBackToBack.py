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
            print(yearInt)
            yearD = 1
            if(yearInt + 1 >= 2020 and yearInt < 2020):
                yearInt = yearInt + 2
                yearD = yearD + 2
            print(yearInt, yearD)    
            teamsWonNext = loaded_data[i+yearD][str(yearInt + 1) + eventMinusYear]
            for team in teamsWonThis:
                if(team in teamsWonNext):
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
            pass
        print(team, year)
        teamsAlreadySeen.append(team)

#print(backToBackYearTeams)
#results of analysis https://docs.google.com/spreadsheets/d/1gpwu8wPT218e3WQY1XekahS6zwPsodvSDgcMBg6xwn4/edit?usp=sharing