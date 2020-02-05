# ****
# author: DAVIDE DI LECCE - Applica s.r.l.
# ****

#https://repl.it/@DavideDi5/Torneo

import random
import time

players = ["Mario Liuzzi", "Michele Leone", "Alessio Grossi", "Marco Colucci", "Gianni Petrosino", "Giovanni Viggiani", "Fabio Latorre",
           "Davide D'Angelo", "Davide Di Lecce", "Angelo D'alconzo", "Michele Gramegna", "Lorenzo Linzalone", "Giuseppe Lapolla", "Bruno Fortunato"]

min = 0
max = len(players)

numbers = []

firsttime = True

for x in range(min, max):
    r = random.randrange(min, max, 1)
    if firsttime:
        numbers.append(r)
    else:
        while (r in numbers):
            r = random.randrange(min, max, 1)
        numbers.append(r)
    firsttime = False

index = 0
for x in numbers:
    if (index == 0 or index % 2 == 0):
        print("Giocatore 1: " + players[x])
    else:
        print("Giocatore 2: " + players[x] + "\n\n")
    index += 1
    time.sleep(2.5)
