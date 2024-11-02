# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import time

players = ["x,y,z"]

teams = ["Juventus", "Milan", "Inter", "Napoli", "Bologna", "Atalanta", "Bayern Munchen", "Borussia Dortmund", "Bayer Leverkusen", "Barcellona", "Atletico Madrid", "Real Madrid", "PSG", "Chelsea", "Arsenal", "Tottenham", "Man City", "Man Utd", "Liverpool"]

min = 0 
max = len(players)

numbers = []
numbers_team = []

firsttime = True
firsttime_team = True

for x in range(min, max):
    r = random.randrange(min, max, 1)
    if firsttime:
        numbers.append(r)
    else:
        while (r in numbers):
            r = random.randrange(min, max, 1)
        numbers.append(r)
    firsttime = False
   
#for x in range(min, max):
#    r = random.randrange(min, max, 1)
#    if firsttime_team:
#        numbers_team.append(r)
#    else:
#        while (r in numbers_team):
#            r = random.randrange(min, max, 1)
#        numbers_team.append(r)
#    firsttime_team = False

index = 0
for x in numbers:
    print("Player: " + players[x])
    print("Team: " + teams[random.randrange(0, len(teams) - 1, 1)] + "\n\n")
    #index += 1
    time.sleep(2.5)
