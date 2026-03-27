import pickle

backToBack = []

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

for year in loaded_data:
    print(year)
    for event in yeard:
        print(event, year)
        yearInt = int(event[0:4])
        eventMinusYear = event[4:]
        try:
            teamsWonThis = year[event]
            teamsWonNext = year[str(yearInt + 1) + eventMinusYear]
            for team in teamsWonThis:
                if(team in teamsWonNext):
                    backToBack.append((team, eventMinusYear, yearInt))
            #print(eventMinusYear, teamsWonThis, teamsWonNext)
        except:
            pass

print(backToBack)