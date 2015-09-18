import csv
import sys
import copy
import itertools

print("Benvenuto.\nQuesto programma in python ti permette di verificare se gli esami scelti nel tuo piano sono compatibili (no collision).\n\n")

input("Press Enter to continue...")
with open('csvnumesami.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['num'], " ", row['esame'])

stringanum = input("Seleziona gli esami che ti interessa seguire questo semestre (Selezionali i numeri degli esami, separati da spazi, per ordine di priorità, in quanto il software controlla le collisioni nell'ordine di inserimento.): \n")

nums = [int(n) for n in stringanum.split()]
#print(nums)

print("Ecco gli esami selezionati:\n")
with open('csvnumesami.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
     	if int(row['num']) in nums:
     		print(row['num'], " ", row['esame'])

arrayCollision = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]


mylist = []
basic = []

for n in nums:
	with open('csvcorsiNum.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if int(row['esame']) == n:
				basic.append([row['esame'],row['day'],row['hoursStart'],row['hoursEnd']])
	mylist.append(basic)
	basic=[]
"""
permutazioni dell'ordine dell'esame. Potrebbe essere utile nella generazione della soluzione con il maggior numero di esami senza collisioni
print(list(itertools.permutations(mylist)))
"""

print(mylist)
listScartati=[]
flag=True

for esamDatas in mylist:
	backUp = copy.deepcopy(arrayCollision)
	for esamData in esamDatas:
		for j in range(int(esamData[2]), int(esamData[3])+1):
			#print ("Esame", esamData[0], "Giorno",esamData[1], " ","StartHour", j,"EndH ",esamData[3], arrayCollision[j][int(esamData[1])])
			if arrayCollision[j][int(esamData[1])] == 1:
				#print ("\nOPS OPS \nEsame", esamData[0], "Giorno",esamData[1], " ","StartHour", j,"EndH ",esamData[3], arrayCollision[j][int(esamData[1])])
				flag=False
				#print(flag,"\n")
				break
		if flag==True:
			for j in range(int(esamData[2]), int(esamData[3])+1):
				#print ("Sto inserendo...Esame", esamData[0], "Giorno",esamData[1], " ","StartHour", j,"EndH ",esamData[3], arrayCollision[j][int(esamData[1])])
				arrayCollision[j][int(esamData[1])] = 1
		else:
			listScartati.append(esamData[0])
			#print(backUp)
			arrayCollision=copy.deepcopy(backUp)
			flag=True
			break
		flag=True


for array in arrayCollision:
	print(array)


print(listScartati)

for n in listScartati:
	nums.remove(int(n))


print("\n\nEcco gli esami che puoi sostenere senza collisioni:\n")
with open('csvnumesami.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
     	if int(row['num']) in nums:
     		print(row['num'], " ", row['esame'])
